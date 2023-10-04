package Atividades.Externas;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class Testes {
    public static void main(String[] args) {
        List<String> nomes = new ArrayList<>();
        nomes.add("Alice");
        nomes.add("Bob");
        nomes.add("Charlie");
        
        // Usando Consumer para imprimir os nomes
        Consumer<String> imprimirNome = nome -> System.out.println(nome);
        
        // Aplicando o Consumer a cada elemento da lista
        nomes.forEach(imprimirNome);
    }
}
//teste 3