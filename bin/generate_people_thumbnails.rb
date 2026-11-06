#!/usr/bin/env ruby
# Regenerate directory portraits without changing the full-size profile images.
require "fileutils"
require "yaml"

root = File.expand_path("..", __dir__)
members = YAML.safe_load_file(File.join(root, "_data/members.yml"))

members.each do |member|
  next unless member["image"] && member["thumbnail"]

  source = File.join(root, "assets/img", member.fetch("image"))
  target = File.join(root, "assets/img", member.fetch("thumbnail"))
  gravity = member["thumbnail_focus"] == "top" ? "North" : "Center"
  FileUtils.mkdir_p(File.dirname(target))
  system(
    "magick", source, "-auto-orient", "-gravity", gravity,
    "-resize", "330x330^", "-extent", "330x330",
    "-define", "webp:method=6", "-quality", "90", target,
    exception: true
  )
  puts "#{member.fetch('name')}: #{File.size(target)} bytes"
end
