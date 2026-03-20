const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
      }
    }
  },
  { threshold: 0.14 }
);

document
  .querySelectorAll(".hero, .section, .layer, .message, .tool-card")
  .forEach((node) => {
    node.classList.add("reveal");
    observer.observe(node);
  });
