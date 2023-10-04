// - DOM
const lamp = document.querySelector('#lampada')
const bt1 = document.querySelector('#btLigar')
const bt2 = document.querySelector('#btDesligar')

// - Evento
bt1.addEventListener('click', ligar)
bt2.addEventListener('click', desligar)

// - Funções

function ligar(){
    lamp.src = 'images/acesa.gif'
}

function desligar(){
    lamp.src = 'images/apagada.gif'
}