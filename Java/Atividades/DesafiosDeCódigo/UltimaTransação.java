package Atividades.DesafiosDeCódigo;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class UltimaTransação {
    
  public static void main(String[] args) {
    try (Scanner scanner = new Scanner(System.in)) {
        String entrada = scanner.nextLine();
        String[] partes = entrada.split(",");
        List <String> parteList = new ArrayList<>();
        for (String parte : partes) {
            parteList.add(parte);
        }
        String parte1 = parteList.get(0);
        String parte2 = parteList.get(1);
        String parte3 = parteList.get(2);
        double parte4 = Double.parseDouble(parteList.get(3));
        Transacao transacao = new Transacao(parte1, parte2, parte3, parte4);
        
        //  Solicitar ao usuário que forneça os valores necessários para criar uma Transacao.
        transacao.imprimir();
    } catch (NumberFormatException e) {
        
    }
  }
}

class Transacao {
  private String data;
  private String hora;
  private String descricao;
  private double valor;

  public Transacao(String data, String hora, String descricao, double valor) {
    this.data = data;
    this.hora = hora;
    this.descricao = descricao;
    this.valor = valor;
  }

  
  
  public void imprimir() {
    System.out.println(this.descricao);
    System.out.println(this.data);
    System.out.println(this.hora);
    System.out.printf("%.2f", this.valor);
  }
}