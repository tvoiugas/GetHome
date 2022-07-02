const navUL = document.getElementById("nav-links");
const navLinks = document.querySelectorAll('.nav-link');

const firstNav = document.getElementById("first-navbar");
const secondNav = document.getElementById("second-navbar");


navLinks.forEach(function (navLink) {
	navLink.addEventListener('click', function () {
		navLinks.forEach(element => element.classList.remove('active'))
		navLink.classList.add('active');
	});
});

let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
	if (lastScrollY < window.scrollY) {
		firstNav.style.top = "-60px";
		secondNav.style.top = "0";
	} else {
		firstNav.style.top = "0px";
		secondNav.style.top = "60px";
	};

});