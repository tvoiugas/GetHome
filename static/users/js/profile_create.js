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

$("#img-input").change(function(){
    readURL(this);
});