$(document).ready(function () {
    $('.navbar li a').css({ "color": "white" });
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('.navbar li a').css({ "color": "black" });
            $(".navbar").removeClass("navbar-light bg-transparent").addClass("navbar-light bg-light");

        } else {
            $('.navbar li a').css({ "color": "white" });
            $(".navbar").removeClass("navbar-light bg-light").addClass("navbar-light bg-transparent");

        }
    });
});