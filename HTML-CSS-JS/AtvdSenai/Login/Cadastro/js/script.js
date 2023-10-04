const bt1 = document.querySelector('#btLogin')
const usuario = document.querySelector('.usuario')
const rusuario = document.querySelector('.rusuario')
const senha = document.querySelector('.senha')
const resenha = document.querySelector('.resenha')

bt1.addEventListener('click', logar)

function logar(){
      let usuario1 = usuario
      let rusuario1 = rusuario
      let senha1 = senha
      let resenha1 = resenha
      
      if (usuario1 == rusuario1 && senha1 == resenha1) {
            window.alert('Usuário cadastrado');
      } 
      else if(usuario1 != rusuario1 || senha1 != resenha1){
            window.alert('Senha ou usuário incorreto');
      }
      
    
}

