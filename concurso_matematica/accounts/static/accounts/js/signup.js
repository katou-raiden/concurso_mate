"use strict";
window.onload = function(e){ 

    //GLOBAL VARIABLES//
    var form = document.querySelector('.form-area');
    var stepArea = document.querySelector('.steps-area');
    var nextButtons = document.querySelectorAll('.next-button');
    var prevButtons = document.querySelectorAll('.prev-button');
    var slides = [];
    var pointer = 0;
    var completed = -1;
    var p = null;
    /***********************/

    //EVENT HANDLERS
    var prevNext = (e) => {
        //Creando e inicializando variable para almacenar el posible proximo slide.
        let sibling = null;
        let formSlide = null;
        

        if (e.target.classList.contains('next-button')) {
            //obteniendo el slide actual
            formSlide = slides[pointer];

            if (validateSteps(formSlide)) {
                //Si todos los campos son validos, proceder.
                if (pointer <= slides.length - 2) {
                    //Si el puntero se encuentra en la penultima posicion, obtener el proximo slide.
                    
                    sibling = slides[pointer + 1];
                }
                else{
                    alert(pointer);
                }

                if (sibling != null) {
                    //Si el proximo slide existe, pues hacer visible el proximo y esconder el actual.
                    sibling.style.display = "flex";
                    formSlide.style.display = "none";
                    
                    if (stepArea.children[pointer].classList.contains('step-active'))
                        stepArea.children[pointer].classList.remove('step-active');
                    
                    stepArea.children[pointer].classList.add('step-completed');
                    stepArea.children[pointer+1].classList.add('step-active');

                    //Almacenar la ultima slide completada con exito
                    if (pointer > completed)
                        completed = pointer;

                    if (p != null)
                        //eliminando text de error pues ya es correcto el paso
                        p.parentElement.remove(p);
                    //posicionando el puntero al siguiente paso del formulario
                    pointer++;
                }

            } 
            else if (p == null) {
                //Si no es valido el slide, y no hay mensaje de error, crear y mostrar uno.
                p = document.createElement('p');
                p.id = "cannot-proceed-text";
                p.innerText = "No puedes avanzar con campos de información erróneos.";
                p.style.color = "red";
                formSlide.appendChild(p);
            }
            
        }
        else if (e.target.classList.contains('prev-button')) {

            //obteniendo el slide actual
            formSlide = e.target.parentElement.parentElement;
                
                if (pointer >= 1) {
                    //Si el puntero se encuentra en mayor que o en la segunda posicion, obtener el anterior slide.
                    sibling = slides[pointer - 1];
                }

                if (sibling != null) {
                    
                    //Si el anterior slide existe, pues hacer visible el anterior y esconder el actual.
                    formSlide.style.display = "none";
                    sibling.style.display = "flex";

                    if (stepArea.children[pointer].classList.contains('step-active')){
                        alert('s');
                        stepArea.children[pointer].classList.remove('step-active');
                    }
            
                    stepArea.children[pointer].style.backgroundColor = "white";
                    stepArea.children[pointer-1].style.backgroundColor = "green";

                    if (p != null)
                        //eliminando text de error pues ya es correcto el paso
                        p.parentElement.remove(p);

                    //posicionando el puntero al anterior paso del formulario
                    pointer--;
            
                }


        }

    };

    var getSlide = (event) => {

        let step = event.target;
        let slideNumber = Number.parseInt(step.getAttribute('value'));
        let nextSlide = null;
        let actualSlide = null;
        
        if (slideNumber <= completed+1 && slideNumber != pointer) {
            //Si el numero de la ultima slide completada es mayor igual a la slide solicitada entonces, proceder.
            nextSlide = slides[slideNumber];
            actualSlide = slides[pointer];
            actualSlide.style.display = "none";
            nextSlide.style.display = "flex";
            pointer = slideNumber;
            if (stepArea.children[pointer].classList.contains('step-completed'))
                stepArea.children[pointer].classList.remove('step-completed');
            stepArea.children[pointer].classList.add('step-active');
            
            
        }


    }
    /*****************************************/

    function init() {

        let step;
        let slidesAmount = form.children.length;

        for (let x = 1; x < slidesAmount; x++) {
            slides.push(form.children[x]);
            step = document.createElement('button');
            step.classList.add('step');
            step.addEventListener('click', getSlide);
            stepArea.appendChild(step);

            if (x > 1) {
                form.children[x].style.display = "none";
            }
        
            if (x < slidesAmount-1) {
                nextButtons[x - 1].addEventListener('click', prevNext);
                prevButtons[x - 1].addEventListener('click', prevNext);
            }

            stepArea.children[x - 1].setAttribute('value', x-1);
        }

        //iniciando el puntero de slide en 0 (cual es el primer slide)
        pointer = 0;

        //iniciando primer slide del formulario y marcando el primer marcador paso
        step = stepArea.children[pointer];
        step.classList.add('step-active');


    }

    function validateSteps(slide) {
        let correct = true;
        for (let x of slide.children) {
            if (x.nodeName == "INPUT" && !x.reportValidity()) {
                if (correct)
                    correct = false;
                x.style.borderBottomColor = "crimson";
            }
        }
        if (correct)
            return true;
        return false;
    }

    init();

};