console.log('JS file 1.js added successfully!');

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");
var paragraf = document.getElementById("hood");
// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
    paragraf.style.marginTop = 50 + 'px'

  } else {
    navbar.classList.remove("sticky");
    paragraf.style.marginTop = 0 + 'px'
  }
}