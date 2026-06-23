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
    window.addEventListener("scroll", function () {
      if (window.scrollY > 30) {
        navbar.style.backgroundColor = "rgba(11, 37, 69, 0.98)";
      } else {
        navbar.style.backgroundColor = "rgba(11, 37, 69, 0.95)";
      }
    });
  }
});
