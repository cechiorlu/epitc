// Page scroll up

var scrollBtn = document.getElementById("scroll-up");
var scrollableDiv = document.getElementById("results");


scrollableDiv.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (scrollableDiv.scrollTop > 10) {
        scrollBtn.style.display = "block";
    } else {
        scrollBtn.style.display = "none";
    }
}

scrollBtn.addEventListener('click', scrollUp);

function scrollUp() {
    scrollableDiv.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}