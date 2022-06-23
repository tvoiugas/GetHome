const hamburger = document.getElementById('hamburger-btn');
const navUL = document.getElementById("nav-ul");

hamburger.addEventListener('click', () => {
	navUL.classList.toggle('show');
});

const navLinks = document.querySelectorAll('.navbar-link');
navLinks.forEach(function (navLink) {
	navLink.addEventListener('click', function () {
		navLinks.forEach(element => element.classList.remove('active'))
		navLink.classList.add('active');
	});
});
