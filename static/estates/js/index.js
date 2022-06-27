const imageBlocks = document.querySelectorAll('.image-container');
const next = document.getElementById('next');

let slideIndex = 0;
showSlide(slideIndex);

function nextSlide() {
	let futureSlide = slideIndex + 1;
	if (imageBlocks[futureSlide]) {
		imageBlocks[slideIndex].classList.remove('active');
		showSlide(slideIndex += 1);
	} else {
		imageBlocks[slideIndex].classList.remove('active');
		slideIndex = 0;
		showSlide(slideIndex);
	};
};

function showSlide() {
	if (imageBlocks[slideIndex]) {
		imageBlocks[slideIndex].classList.add('active');
	};
};

$('.carousel').carousel()

next.addEventListener('click', nextSlide);
