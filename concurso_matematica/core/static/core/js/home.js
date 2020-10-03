
/*var slideShowSlides = document.getElementById('slideShow-slides');
var slideShowSlidesStyle = getComputedStyle(slideShowSlides, null);
var slideShowSlidesWidth = slideShowSlidesStyle.width;
var slideShowSlidesHeight = slideShowSlidesWidth / 1.777;
slideShowSlides.style.height = slideShowSlidesHeight.toString();

var slideIndex = 1;


// Next/previous controls
function plusSlides(n) {

  showSlides(slideIndex += n);

}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slide");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";


}
showSlides(slideIndex);

*/
var texts = document.getElementsByClassName('card-text');
var readMoreButton = document.getElementsByClassName('read-more');
let expression = /\d+/;

let count = 0;
for (let x of texts) {
  console.log(x);
  $clamp(x, { clamp: 4, animate: true });
}

for (let x = 0; x < texts.length; x++) {

  if (Math.ceil(expression.exec(getComputedStyle(texts[x], null).height) / expression.exec(getComputedStyle(texts[x], null).lineHeight)) >= 4) {
    readMoreButton[x].classList.replace('d-none', 'd-inline-block');
  }

}


