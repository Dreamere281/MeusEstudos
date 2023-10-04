package Atividades.DesafiosDeCódigo;
import java.util.Scanner;

public class JurosCompostos {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            double valor = scanner.nextDouble();

            if (valor > 0) {
                System.out.printf("Deposito realizado com sucesso!%nSaldo atual: R$ %.2f%n", valor);
                
            } else if (valor == 0) {
                 System.out.println("Encerrando o programa...");
            } else if (valor <= 0) {
                 System.out.println("Valor invalido! Digite um valor maior que zero.");

            }
        }
    }
}