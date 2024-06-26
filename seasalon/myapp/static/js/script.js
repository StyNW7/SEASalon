// Image slider

let carsImage = 1;

displaying(carsImage);

function currentSlide(n){

    displaying(carsImage = n)

}

function displaying(n){

    let i;
    let image = document.getElementsByClassName("image");
    let dots = document.getElementsByClassName("dot");

    if(n > image.length){
        carsImage = 1;
    }

    if(n < 1){
        carsImage = image.length;
    }

    for(i=0; i < image.length; i++){
        image[i].style.display = "none";
    }

    for(i=0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace(" active", "");
    }

    image[carsImage - 1].style.display ="block";
    dots[carsImage - 1].className += " active";

}
