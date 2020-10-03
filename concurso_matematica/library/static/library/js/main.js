
var carouselInner = document.querySelector('.carousel-inner');
var cards = carouselInner.querySelectorAll('.card');
var mode = undefined;



window.onresize = function (evt) {
    arrangeCards(carouselInner, cards, window.innerWidth);
}

var arrangeCards = (container, cards, size) => {

    if (container == null || container == undefined) {
        alert('error');
    } else {


        let counter = 0;
        let row = null;
        let item = null;


        if (size >= 320 && size < 768 && mode !== 1) {

            let carouselItems = carouselInner.querySelectorAll('.carousel-item');

            if (carouselItems !== null) {
                for (let item of carouselItems) {
                    carouselInner.removeChild(item);
                }
            }

            for (let card of cards) {
                item = document.createElement('div');
                item.className = 'carousel-item';
                if (counter == 0) {
                    item.className = item.className + ' active';
                }
                row = document.createElement('div');
                row.className = 'row';
                row.appendChild(card);
                item.appendChild(row);
                container.appendChild(item);
                counter++;
            }

            mode = 1;

        } else if (size >= 768 && size < 992 && mode !== 2) {
            counter = 0;
            let firstTime = true;
            let column = null;

            for (let card of cards) {
                if (counter <= 0) {

                    if (!firstTime) {
                        container.appendChild(item);
                    }

                    item = document.createElement('div');
                    item.className = 'carousel-item';
                    row = document.createElement('div');
                    row.className = 'row';
                    row.appendChild(card);
                    item.appendChild(row);

                    if (firstTime) {
                        item.className = item.className + ' active';
                        firstTime = false;
                    }

                    counter = 2;

                } else {
                    column = document.createElement('div');
                    column.className = 'col-md-6';
                    column.appendChild(card);
                    row.appendChild(column);
                    counter--;
                }
            
            }
            
            mode = 2;

        }

        else if (size >= 992 && size < 1200 && mode !== 3) {
            if (carouselItems !== null) {
                for (let item of carouselItems) {
                    carouselInner.removeChild(item);
                }
            }

            counter = 0;
            let firstTime = true;
            let column = null;

            for (let card of cards) {
                if (counter <= 0) {

                    if (!firstTime) {
                        container.appendChild(item);
                    }

                    item = document.createElement('div');
                    item.className = 'carousel-item';
                    row = document.createElement('div');
                    row.className = 'row';
                    row.appendChild(card);
                    item.appendChild(row);

                    if (firstTime) {
                        item.className = item.className + ' active';
                        firstTime = false;
                    }

                    counter = 3;

                } else {
                    column = document.createElement('div');
                    column.className = 'col-md-6';
                    column.appendChild(card);
                    row.appendChild(column);
                    counter--;
                }
            
            }


            mode = 3;

        } else if (size >= 1200 && mode !== 4) {
            if (carouselItems !== null) {
                for (let item of carouselItems) {
                    carouselInner.removeChild(item);
                }
            }

            counter = 0;
            let firstTime = true;
            let column = null;

            for (let card of cards) {
                if (counter <= 0) {

                    if (!firstTime) {
                        container.appendChild(item);
                    }

                    item = document.createElement('div');
                    item.className = 'carousel-item';
                    row = document.createElement('div');
                    row.className = 'row';
                    row.appendChild(card);
                    item.appendChild(row);

                    if (firstTime) {
                        item.className = item.className + ' active';
                        firstTime = false;
                    }

                    counter = 4;

                } else {
                    column = document.createElement('div');
                    column.className = 'col-md-6';
                    column.appendChild(card);
                    row.appendChild(column);
                    counter--;
                }
            
            }

            mode = 4;
        }

    }
}
