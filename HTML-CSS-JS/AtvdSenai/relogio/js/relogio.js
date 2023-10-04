//DOM
const horas = document.querySelector('#horas')
const minutos = document.querySelector('#minutos')
const segundos = document.querySelector('#segundos')
const milisegundos = document.querySelector('#milisegundos')

//EVENTOS
setInterval(relogio, 1000)

//FUNÇÕES

function relogio(){
    let hoje = new Date()
    let hr = hoje.getHours()
    let min = hoje.getMinutes()
    let sec = hoje.getSeconds()
    let mili = hoje.getMilliseconds()


    if (hr<10)
        hr = "0" + hr;
	if (min < 10)
		min = "0" + min;
	if (sec < 10)
		sec = "0" + sec;

	if (mili < 10)
		mili = "00" + mili;
	else if (mili < 100)
		mili = "0" + mili;

    horas.textContent = hr
    minutos.textContent = min
    segundos.textContent = sec
    milisegundos.textContent = mili
}

