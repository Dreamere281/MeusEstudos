package Atividades.DesafiosDeCódigo;
import java.util.ArrayList;
import java.util.Scanner;

public class BancoOrganizadorAtivos {
  public static void main(String[] args) {
    try (Scanner scanner = new Scanner(System.in)) {
      var ativos = new ArrayList <String > ();

      //Entrada dos tipos de ativos
      int quantidadeAtivos = scanner.nextInt();

      // Entrada dos códigos dos ativos
      for (int i = 0; i < quantidadeAtivos; i++) {
        String codigoAtivo = scanner.nextLine();
        ativos.add(codigoAtivo);
      }
      sort(ativos);
      for(String ativo : ativos){
      System.out.println(ativo);
      }

  
    }
  }

  private static void sort(ArrayList<String> ativos) {
  }  
}
//1