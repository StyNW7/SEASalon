// Back to Top Button

let mybutton = document.getElementById("backToTop");

window.onscroll = function () { scrollFunction() };

function scrollFunction() {

    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        mybutton.style.display = "block";

    } 
    
    else {
        mybutton.style.display = "none";
    }
}