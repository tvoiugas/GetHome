function incEltNbr(id) {
	elt = document.getElementById(id);
	endNbr = Number(elt.getAttribute('data-end-value'));
	startNbr = Math.round(endNbr / 2);
	speed = Number(elt.getAttribute('data-speed'));
	incNbrRec(startNbr, endNbr, elt, speed);
};


function incNbrRec(i, endNbr, elt, speed) {
	if (i <= endNbr) {
    	elt.innerHTML = i;
    	setTimeout(function() {
    		incNbrRec(i + 1, endNbr, elt, speed);
    	}, speed);
  	};
};

$(document).ready(function () {
	incEltNbr("homes");
	incEltNbr("awards");
	incEltNbr("followers");
	incEltNbr("rentals");
});