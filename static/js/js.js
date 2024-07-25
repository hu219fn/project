let up = document.getElementById('up');
let ul_sections = document.getElementById('ul-sections');

up.style.display = 'block';
ul_sections.style.display = 'none';

up.onclick = ()=>{
    if (ul_sections.style.display == 'none'){
        ul_sections.style.display = 'block'
    }else {
        ul_sections.style.display = 'none'
    }
}
let up0 = document.getElementById('up0');
let ul_sections0 = document.getElementById('ul-sections0');

up0.style.display = 'block';
ul_sections0.style.display = 'none';

up0.onclick = ()=>{
    if (ul_sections0.style.display == 'none'){
        ul_sections0.style.display = 'block'
    }else {
        ul_sections0.style.display = 'none'
    }
}

////

let menu = document.getElementById('menu');
let ul_display = document.getElementById('ul-display');
let icons = [...document.getElementsByClassName('icons')];
menu.onclick = ()=>{
    if (ul_display.style.display == 'block'){
        icons.forEach(icon=>()=>{
            icon.style.display = 'none';
        })
        ul_display.style.display = 'none';
    }else {
        ul_display.style.display = 'block';
    }
}


/////
try {
    let title = document.getElementById('title').innerHTML;
    let mhh1 = document.getElementById('mhh1');
    mhh1.innerHTML = 'Users who requested \"' + title + '\"';
}catch(err){
    console.log(' ');
}


//////
try {
    let minus = document.getElementById('minus');
    let plus = document.getElementById('plus');
    let num = document.getElementById('count');
    
    minus.onclick = ()=>{
        var number = +num.value;
        if(number > 1) {
            var number0 = number - 1;
            num.value = number0;
        }
    }
    plus.onclick = ()=>{
        var number = +num.value;
        var number0 = number + 1;
        num.value = number0;
    }
}catch(err){
    console.log(' ');
}

//////
try {
    let b = [...document.getElementsByClassName('b')];
    let result = 0;
    b.forEach(order=>
        result += +order.innerHTML
    )
    document.getElementById('total').innerHTML = result + ' IRQ';
}catch {
    console.log(' ');
}