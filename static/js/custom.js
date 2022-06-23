const hamburger = document.getElementById('hamburger-btn');
const navUL = document.getElementById("nav-ul");

hamburger.addEventListener('click', () => {
	navUL.classList.toggle('show');
});