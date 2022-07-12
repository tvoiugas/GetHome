const navLinks = document.querySelectorAll('.nav-link');

const firstNav = document.getElementById("first-navbar");
const secondNav = document.getElementById("second-navbar");
const hamburgerBtn = document.getElementById('hum-btn');
const menu = document.getElementById('menu');
const menuCloseBtn = document.getElementById('menu-close');

$(document).ready(function () {
	var url = window.location;
	navLinks.forEach(function (navLink) {
		if (navLink.href == url) {
			navLink.classList.add('active');
		};
	});
});

let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
	var actualDisplay = getComputedStyle(firstNav).display;
	if (actualDisplay == 'flex') {
		if (lastScrollY < window.scrollY) {
			firstNav.style.top = "-60px";
			secondNav.style.top = "0";
		} else {
			firstNav.style.top = "0px";
			secondNav.style.top = "60px";
		};
	} else {
		secondNav.style.top = '0px';
	};
});

function OpenNav() {
	if (menu.classList.contains('active')) {
		mwnu.classList.remove('active');
	} else {
		menu.classList.add('active');
	};
};

function CloseNav() {
	menu.classList.remove('active');
}


hamburgerBtn.addEventListener('click', OpenNav);
menuCloseBtn.addEventListener('click', CloseNav);