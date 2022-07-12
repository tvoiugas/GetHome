var sortBtn = document.getElementById('actual-btn');
const sortUl = document.getElementById('sort-ul');
const sortLis = document.querySelectorAll('#sort-li');

var type = 'off';

function ShowUl() {
	var condition = sortUl.getAttribute('data-condition');

	if (condition === 'on') {
		sortUl.style.opacity = 0;
		sortUl.style.visibility = 'hidden';
		sortUl.setAttribute('data-condition', 'off');
	} else {
		sortUl.style.opacity = 1;
		sortUl.style.visibility = 'visible';
		sortUl.setAttribute('data-condition', 'on');
	};

};

function ChangeSortBtn(evt) {
	sortBtn.innerHTML = evt.currentTarget.innerHTML;
	ShowUl();
};

sortLis.forEach(function (sortLi) {
	sortLi.addEventListener('click', ChangeSortBtn);
});

sortBtn.addEventListener('click', ShowUl);