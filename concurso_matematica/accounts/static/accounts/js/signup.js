var form = document.querySelector('.form-area');
        var stepArea = document.querySelector('.steps-area');
        var nextButtons  = document.querySelectorAll('.next-button');
        var prevButtons  = document.querySelectorAll('.prev-button');

        var prevNext = (e) => {
            if(e.target.classList.contains('next-button')){
                formSlide = e.target.parentElement.parentElement;
                sibling = formSlide.nextElementSibling;
                if(sibling !== undefined) {
                    formSlide.style.display = "none";
                    sibling.style.display = "block"

                } 
            }
            else if(e.target.classList.contains('prev-button')){
                formSlide = e.target.parentElement.parentElement;
                sibling = formSlide.previousElementSibling;
                if(sibling !== undefined) {
                    formSlide.style.display = "none";
                    sibling.style.display = "block"

                } 

            }
        };
        function init(){
        
        for(let x=1; x<form.children.length; x++)
        {
            form.children[x].style.display = "none";
            step = document.createElement('button');
            step.classList.add('step');
            stepArea.appendChild(step);
        }
        for(let x=0; x<nextButtons.length; x++){
            nextButtons[x].addEventListener('click', prevNext);
            prevButtons[x].addEventListener('click', prevNext);
        }
        
        }

        init();