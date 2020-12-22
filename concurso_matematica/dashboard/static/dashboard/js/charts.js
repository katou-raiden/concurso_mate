


function randomNum() {
    return Math.floor(Math.random() * 256);
}

function randomRGB() {
    var red = randomNum();
    var green = randomNum();
    var blue = randomNum();
    return [red, green, blue];
}

function buildCharts(box, data) {
    let chartBox = document.getElementById(box);
    let bars = new DocumentFragment();
    let count = 0;
    Object.entries(data).forEach(element => {
        let name = element[0];
        let values = element[1];
        let result = values[0] / values[1] * 100;
        let bar = document.createElement('div');
        bar.className = "bar";
        bar.id = "bar" + (count+1).toString();
        let barValue = document.createElement('span');
        let barValueNumber = document.createElement('span');
        result = Math.trunc(result);
        barValue.style.width = result.toString()+'%';
        barValue.className = "value";
        barValueNumber.textContent = result.toString()+"%";
        barValueNumber.className = "valueNumber";
        let barName = document.createElement('span');
        barName.className = "name";
        barName.textContent = name;
        let barBox = document.createElement('div');
        barBox.className = "barBox";
        barBox.appendChild(barValue);
        bar.appendChild(barName);
        bar.appendChild(barBox);
        bar.appendChild(barValueNumber);
        let rgb = randomRGB();
        barValue.style.backgroundColor = "rgb(" + rgb[0] + ", " + rgb[1] + ", " + rgb[2] + ")";
        bars.appendChild(bar);
        bars.appendChild(document.createElement('div'));
        count++;

    });

    chartBox.appendChild(bars);
}



