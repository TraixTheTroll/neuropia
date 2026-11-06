#!/usr/bin/env ruby
# Validate the generated Neuropia site without relying on external websites.
require "yaml"
require "nokogiri"
require "uri"
require "pathname"

root = Pathname.new(ARGV.fetch(0, "_site")).expand_path
members = YAML.safe_load_file("_data/members.yml")
config = YAML.safe_load_file("_config.yml")
origin = URI(config.fetch("url"))
errors = []
pages = ["index.html", "404.html", *%w[research people publications contact].map { |x| "#{x}/index.html" }]
pages.concat(members.map { |member| "people/#{member.fetch('slug')}/index.html" })
actual = root.glob("**/*.html").map { |path| path.relative_path_from(root).to_s }.reject { |path| path.start_with?("assets/") }
errors << "Public page set changed: #{actual.sort.inspect}" unless actual.sort == pages.sort

pages.each do |relative|
  file = root.join(relative)
  unless file.file?
    errors << "Missing page: #{relative}"
    next
  end
  document = Nokogiri::HTML(file.read)
  errors << "Missing main heading: #{relative}" unless document.at_css("main h1")
  errors << "Missing page title: #{relative}" if document.at_css("title")&.text.to_s.strip.empty?
  errors << "Timed redirect: #{relative}" if document.at_css('meta[http-equiv="refresh"]')
  document.css("[href], [src]").each do |node|
    value = node["href"] || node["src"]
    next if value.nil? || value.empty? || value.start_with?("mailto:", "tel:", "data:")

    begin
      url = URI.join("#{origin}/#{relative}", value)
      next unless url.host == origin.host

      target = root.join(URI::DEFAULT_PARSER.unescape(url.path).delete_prefix("/"))
      target = target.join("index.html") if target.directory?
      unless target.file?
        errors << "Broken local link in #{relative}: #{value}"
        next
      end
      if url.fragment && target.extname == ".html"
        id = URI::DEFAULT_PARSER.unescape(url.fragment)
        target_document = target == file ? document : Nokogiri::HTML(target.read)
        errors << "Missing anchor in #{relative}: #{value}" unless target_document.css("[id]").any? { |element| element["id"] == id }
      end
    rescue URI::InvalidURIError => error
      errors << "Invalid URL in #{relative}: #{value} (#{error.message})"
    end
  end
end

members.each do |member|
  slug = member.fetch("slug")
  image = "/assets/img/#{member.fetch('image')}"
  thumbnail = "/assets/img/#{member.fetch('thumbnail')}"
  profile = root.join("people/#{slug}/index.html")
  if profile.file?
    document = Nokogiri::HTML(profile.read)
    errors << "Wrong full-size profile image: #{slug}" unless document.at_css(".neuropia-profile-photo")&.[]("src") == image
  end
  ["index.html", "people/index.html"].each do |relative|
    next unless root.join(relative).file?

    document = Nokogiri::HTML(root.join(relative).read)
    card = document.css(".person").find { |node| node["href"] == "/people/#{slug}/" }
    errors << "Wrong directory thumbnail: #{relative} #{slug}" unless card&.at_css("img")&.[]("src") == thumbnail
  end
end

keys = File.read("_bibliography/neuropia.bib").scan(/^@\w+\s*\{\s*([^,\s]+),/).flatten
["index.html", "publications/index.html"].each do |relative|
  next unless root.join(relative).file?

  actual_keys = Nokogiri::HTML(root.join(relative).read).css("article.pub").map { |node| node["id"] }
  errors << "Publication list does not match bibliography: #{relative}" unless actual_keys.sort == keys.sort
end

errors << "Wrong custom domain" unless root.join("CNAME").file? && root.join("CNAME").read.strip == "neuropia.no"
%w[bin test output docs sources vendor node_modules].each do |name|
  errors << "Private build/source directory published: #{name}" if root.join(name).exist?
end
abort(errors.join("\n")) unless errors.empty?
puts "Site checks passed: #{pages.length} pages, #{members.length} profiles, #{keys.length} publications; local links, assets and anchors valid."
