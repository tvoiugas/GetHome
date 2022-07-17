let submitBtn = document.getElementById('submit-btn');
let stepBtn = document.getElementById('step-btn');

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img-show').attr('src', e.target.result);
            $('#img-show').attr('style', 'display: block;');

        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_photo").change(function(){
    readURL(this);
});


submitBtn.addEventListener('click', submitAndStep);

function submitAndStep() {
	stepBtn.click();
};

function clickStepBtn(id) {
	stepBtn = document.getElementById(id);
	stepBtn.click();
};