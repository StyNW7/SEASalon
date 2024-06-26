// Header Function START

window.addEventListener("scroll", function(){

    const header = document.querySelector("header");

    header.classList.toggle("sticky", window.scrollY > 5);
})

// Menu Toggle

function menu(){

    const menuToggle = document.querySelector(".menuToggle");
    const navigation = document.querySelector(".navigation");

    menuToggle.classList.toggle("active");
    navigation.classList.toggle("active");

}

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