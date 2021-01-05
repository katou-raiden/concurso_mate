
window.addEventListener('load', function () {

    var exercises = document.getElementsByClassName('exercise');
    var nextBtn = document.getElementById('next-btn');
    var prevBtn = document.getElementById('prev-btn');
    var active = 0;
    var radioBtns = [];
    var radioBox = document.getElementById('radio-box');
    var submitBtn = document.querySelector('button[type="submit"]');
    console.log(submitBtn);
    var submitQuestion = document.getElementById('submit-question');
    var selectInputs = document.getElementsByClassName('form-control');
    var form = document.querySelector('form');
    var ruleBtns = document.querySelectorAll('.accept-rule-btn');


    function putModalsAtBodyEnd() {
        let modals = document.querySelectorAll('.modal');
        for (let x = 0; x < modals.length; x++) {
            modals[x].remove();
            document.body.append(modals[x])
        }

    }



    function getExercise(evt) {

        let selected = Number.parseInt(evt.target.id.charAt(1));

        if (!radioBtns[selected].classList.contains('active')) {

            exercises[selected].style.display = "block";
            radioBtns[selected].classList.add('active');
            exercises[active].style.display = "none";
            radioBtns[active].classList.remove('active');
            active = selected;

        }

    }

    function nextPrev(evt) {
        if (evt.target.id == 'next-btn') {
            if (exercises.length - 1 > active) {
                exercises[active].style.display = "none";
                exercises[active + 1].style.display = "block";
                radioBtns[active].classList.remove('active');
                radioBtns[active + 1].classList.add('active');
                active += 1;
            }

        } else if (evt.target.id == 'prev-btn') {
            if (0 < active) {
                exercises[active].style.display = "none";
                exercises[active - 1].style.display = "block";
                radioBtns[active].classList.remove('active');
                radioBtns[active - 1].classList.add('active');
                active -= 1;
            }
        }
    }

    function initialize() {

        putModalsAtBodyEnd();
        let radio = null;


        for (let x = 0; x < exercises.length; x++) {
            exercises[x].style.display = "none";
            
            radio = document.createElement('span');
            radio.className = "radio";
            radioBox.append(radio);
            radioBtns.push(radio);
            radioBtns[x].addEventListener('click', getExercise);
            radioBtns[x].id = 'r' + x;

        }
        exercises[0].style.display = "block";
        radioBtns[0].classList.add('active');
        nextBtn.addEventListener('click', nextPrev);
        prevBtn.addEventListener('click', nextPrev);
        $('[data-toggle="popover"]').popover();

        form.addEventListener('submit', function(e) {
            e.preventDefault();
            let total = 0;
            
            for (let select of selectInputs) {
                total += Number.parseInt(select.value)
            }

            if (confirm(`Tiene acumulado en total ${total}/${selectInputs.length*7} puntos.\nEsta seguro de que desea continuar ?`)) {
                form.submit()
            } 
        });

        let counter = 0;
        for (let ruleBtn of ruleBtns) {
            ruleBtn.selectInput = counter;
            ruleBtn.addEventListener('click', function (e) {
                
                if (selectInputs[e.target.selectInput].hasAttribute('disabled')) {
                    selectInputs[e.target.selectInput].removeAttribute('disabled');
                }
            })
            counter++;
        }

    }

    initialize();

});

