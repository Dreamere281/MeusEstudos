package Atividades.DesafiosDeCódigo;

import java.util.Scanner;

abstract class Cofre {
  protected String tipo;
  protected String metodoAbertura;

  public Cofre(String tipo, String metodoAbertura) {
    this.tipo = tipo;
    this.metodoAbertura = metodoAbertura;
  }

  public void imprimirInformacoes() {
    System.out.println("Tipo: " + this.tipo);
    System.out.println("Metodo de abertura: " + this.metodoAbertura);
  }
}

class CofreDigital extends Cofre {

  private int senha;

  public CofreDigital(int senha) {
    super("Cofre Digital", "Senha");
    this.senha = senha;
  }

  public boolean validarSenha(int confirmacaoSenha) {
    return confirmacaoSenha == this.senha;
  }
}

class CofreFisico extends Cofre {

  public CofreFisico() {
    super("Cofre Fisico", "Chave");
  }

}

public class CofreSeguro {
  public static void main(String[] args) {
    try (// Lê o tipo de cofre (primeira linha da entrada)
    Scanner scanner = new Scanner(System.in)) {
    String tipoCofre = scanner.nextLine();
    
        //  Implemente a condição necessário para a verificação dos cofres seguros:
        if (tipoCofre.equalsIgnoreCase("digital")) {
            int primeiraSenha = scanner.nextInt();
            int segundaSenha = scanner.nextInt();
            CofreDigital cofre = new CofreDigital(primeiraSenha);
            
            cofre.imprimirInformacoes();
            if (cofre.validarSenha(primeiraSenha) != cofre.validarSenha(segundaSenha)) {
                System.out.println("Senha incorreta!"); 
            }
            else{
                System.out.println("Cofre aberto!");
            }
        }
        else if(tipoCofre.equalsIgnoreCase("fisico")){
            Cofre cofre = new CofreFisico();
            cofre.imprimirInformacoes();
        }
        
    }

  }
}