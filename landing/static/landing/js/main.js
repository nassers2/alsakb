document.addEventListener("DOMContentLoaded", function () {
  if (window.AOS) {
    AOS.init({
      duration: 700,
      once: true,
      offset: 80,
    });
  }

  var navbar = document.querySelector(".main-navbar");
  if (navbar) {
    var toggleScrolled = function () {
      navbar.classList.toggle("scrolled", window.scrollY > 30);
    };
    toggleScrolled();
    window.addEventListener("scroll", toggleScrolled);
  }
});
