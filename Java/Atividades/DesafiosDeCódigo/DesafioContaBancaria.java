package Atividades.DesafiosDeCódigo;

import java.util.Scanner;

public class DesafioContaBancaria {

  public static void main(String[] args) {
    try (// Lendo os dados de Entrada:
    Scanner scanner = new Scanner(System.in)) {
        int numeroConta = scanner.nextInt();
        scanner.nextLine(); // Consome a quebra de linha após a entrada do número da conta
        
        String nomeTitular = scanner.nextLine();
        
        double saldo = scanner.nextDouble();

        new ContaBancaria(numeroConta, nomeTitular, saldo);
        

        System.out.println("Informacoes:");
        System.out.println("Conta: "+ numeroConta+"\nTitular: "+ nomeTitular+"\nSaldo: R$ "+ saldo);
    }
    
  }
}

class ContaBancaria {
  int numero;
  String titular;
  double saldo;

  public ContaBancaria(int numero, String titular, double saldo) {
    this.numero = numero;
    this.titular = titular;
    this.saldo = saldo;
  }
}