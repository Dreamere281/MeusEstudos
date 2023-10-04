const imagem = document.querySelector('#imagem')
const jogador = document.querySelector('#nome')
const btha =document.querySelector('#btha')
const btcr7 =document.querySelector('#btcr7')
const btdy =document.querySelector('#btdy')
const btmba =document.querySelector('#btmba')
const btmessi =document.querySelector('#btmessi')
const btgoi =document.querySelector('#btgoi')

btcr7.addEventListener('click',cr7)
btdy.addEventListener('click', dybala)
btmba.addEventListener('click', mbappe)
btmessi.addEventListener('click', messi)
btgoi.addEventListener('click', goiaba)
btha.addEventListener('click', halland)

function halland(){
    imagem.src ='images/haaland.png'
}
function cr7(){
    imagem.src ='images/cr7.jpg'
}
function dybala(){
    imagem.src ='images/dybala.jpg'
}
function mbappe(){
    imagem.src ='images/mbappe.jpg'
}
function messi(){
    imagem.src ='images/messi.jpg'
}
function goiaba(){
    imagem.src ='images/junior-goiaba.webp'
}