// Отображение вкладки по клику

const tabs = document.querySelectorAll('.tab');
const contents = document.querySelectorAll('.tab_content');

for (let i = 0; i < tabs.length; i++) {

    tabs[i].addEventListener ('click', (event) => {

        if (event.target.classList.contains('tab-active')) {

            tabs.forEach(el => {
                el.classList.remove('tab-active');
            });
        }

        else {

            tabs.forEach(el => {
                el.classList.remove('tab-active');
            });

            event.target.classList.add('tab-active');
        }
    })
}

// Количество товара

var InnerNum = 1;
const chBtns = document.querySelectorAll('.q-btn-set');
var changeInp = document.getElementById("num");

window.onload = function() {

for ( let i=0; i < chBtns.length; i++ ) {

    chBtns[i].addEventListener ('click', ( event ) => {

        let value = chBtns[i].value;

        if (value == '−' && InnerNum >= 2) {

            changeInp.value = InnerNum - 1;
            InnerNum--;

        }
        else if (value == '+') {

            changeInp.value = InnerNum + 1;
            InnerNum++;

        }
    });
}
};

// Раскрывающееся меню

// Кнопка "меню"

var menuBtn = document.querySelector('.menuBtn');
var openMenu = document.querySelector('.openedMenu');
var angleLeft = document.querySelector('#leftNav');

menuBtn.onclick = function() {

    openMenu.classList.toggle('showMenu');
    angleLeft.classList.toggle('noAngle');

}

// Кнопка "регистрация"

var loginBtn = document.querySelector('.loginBtn');
var openLogin = document.querySelector('.openedLogin');
var angleRight = document.querySelector('#rightNav');
loginBtn.onclick = function() {

    openLogin.classList.toggle('showLogin');
    angleRight.classList.toggle('noAngle');

    if (openLogin.classList.contains('showLogin')) {
        loginBtn.setAttribute('style', "background-color: #29FD2E; border-radius: 0.375rem;")
    } else {
        loginBtn.removeAttribute('style', "background-color: #29FD2E; border-radius: 0.375rem;")
    }
}

// Анимация формы регистрации

let labels = document.querySelectorAll('.inputContainer label')

labels.forEach(label => {
    label.innerHTML = label.innerText
    .split('')
    .map((letter, idx) => `<span style= "transition-delay:${idx * 30}ms">${letter}</span>`)
    .join('')
})

// Очистка формы

// let regFrom = document.querySelector('#regForm')
// let inputs = document.querySelectorAll('.inputContainer input')



// regFrom.addEventListener('submit', (event) => {
//     inputs.forEach(el => {
//         el.value = "";
//     })

// })