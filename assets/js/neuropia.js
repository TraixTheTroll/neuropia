(() => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const backToTop = document.querySelector(".back-to-top");
  if (backToTop) {
    const updateBackToTop = () => {
      const hidden = window.scrollY <= 120;
      if (backToTop.hidden !== hidden) backToTop.hidden = hidden;
    };
    window.addEventListener("scroll", updateBackToTop, { passive: true });
    updateBackToTop();
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: reducedMotion.matches ? "instant" : "smooth" });
    });
  }

  // Keep readable year headings without JavaScript; enhance them with native toggles.
  document.querySelectorAll(".publication-list > h2.bibliography").forEach((heading) => {
    const papers = heading.nextElementSibling;
    if (!papers?.matches("ol.bibliography")) return;
    const year = document.createElement("details");
    year.className = "publication-year";
    year.open = true;
    const summary = document.createElement("summary");
    heading.before(year);
    summary.append(heading);
    year.append(summary, papers);
  });

  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  let frame;
  let w,
    h,
    particles = [],
    stars = [];

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }
  window.addEventListener("resize", resize);
  resize();

  for (let i = 0; i < 150; i++) {
    stars.push({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.5 + 0.3,
      a: Math.random(),
      speed: Math.random() * 0.3 + 0.05,
    });
  }

  const colors = ["#2ec4b6", "#ff9f1c", "#e07a5f", "#8ecae6", "#ffb703"];
  for (let i = 0; i < 40; i++) {
    particles.push({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 4 + 2,
      color: colors[Math.floor(Math.random() * colors.length)],
      vx: (Math.random() - 0.5) * 0.6,
      vy: (Math.random() - 0.5) * 0.6,
      pulse: Math.random() * Math.PI * 2,
    });
  }

  function animate() {
    // Clear old positions completely so moving circles never leave trails.
    ctx.clearRect(0, 0, w, h);

    stars.forEach((s) => {
      s.a += s.speed * 0.02;
      const alpha = 0.3 + Math.sin(s.a) * 0.5;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${alpha})`;
      ctx.fill();
      s.y -= s.speed * 0.2;
      if (s.y < 0) s.y = h;
    });

    particles.forEach((p) => {
      p.x += p.vx;
      p.y += p.vy;
      p.pulse += 0.03;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;
      const glow = 0.6 + Math.sin(p.pulse) * 0.4;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r * glow, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = 0.7;
      ctx.fill();
      ctx.globalAlpha = 1;
    });

    if (!reducedMotion.matches && !document.hidden) frame = requestAnimationFrame(animate);
  }
  function restart() {
    cancelAnimationFrame(frame);
    animate();
  }
  reducedMotion.addEventListener("change", restart);
  document.addEventListener("visibilitychange", restart);
  restart();
})();
