document.addEventListener('DOMContentLoaded',() => {
    $('.info-resto').hide();
    $('.resto').click(function () {
        $('.resto').hide();
        $('.info-resto-'+this.classList[1]).show();
    });
    $('.esc').click(function (){
        $('.info-resto').hide();
        $('.resto').show();
    });
});