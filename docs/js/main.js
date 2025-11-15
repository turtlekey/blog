(() => {
  // <stdin>
  function goHome() {
    const eleTitle = document.querySelector("#blog-title");
    eleTitle.addEventListener("pointerdown", () => window.location.href = "/blog/");
  }
  document.addEventListener("DOMContentLoaded", function() {
    goHome();
  });
})();
