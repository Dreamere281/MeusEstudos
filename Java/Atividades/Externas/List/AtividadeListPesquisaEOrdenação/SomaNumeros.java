package Atividades.Externas.List.AtividadeListPesquisaEOrdenação;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SomaNumeros {
    
    private List<Integer> numeros;

    public SomaNumeros() {
        this.numeros = new ArrayList<>();
    }

    public void adicionarNumero(int numero){
       this.numeros.add(numero);
    }

    public int calcularSoma(){
        int somaTotal = 0;
            for (Integer i :numeros){
                somaTotal += i;
            }
        return somaTotal;
    }

    public int encontrarMaiorNumero(){
        int maiorValor = Integer.MIN_VALUE;
        if (!numeros.isEmpty()) {
            for (Integer i : numeros) {
                if (i >= maiorValor) {
                    maiorValor = i;   
                }
            }
        } else {
            throw new RuntimeException("A lista está vazia");
        }
        return maiorValor;
    }

    public int encontrarMenorNumero(){
        int menorValor = Integer.MAX_VALUE;
        if (!numeros.isEmpty()) {
            for (Integer i : numeros) {
                if (i <= menorValor) {
                    menorValor = i;
                }
            }
        } else {
            throw new RuntimeException("A lista está vazia");
        }
        return menorValor;
    }

    public void exibirNumeros(){
        if (!numeros.isEmpty()) {
            System.out.println(this.numeros);
        } else {
            System.out.println("A lista está vazia");
        }
    }

    public List<Integer> ordenarCrescente(){
        List<Integer> numerosAscendente = new ArrayList<>(this.numeros);
        if (!numeros.isEmpty()) {
            Collections.sort(numerosAscendente);
        } else {
            System.out.println("A lista está vazia");
        }
        return numerosAscendente;
        
    }

    public List<Integer> ordenarDecrescente(){
        List<Integer> numerosAscendente = new ArrayList<>(this.numeros);
        if (!numeros.isEmpty()) {
            numerosAscendente.sort(Collections.reverseOrder());
        } else {
            System.out.println("A lista está vazia");
        }
        return numerosAscendente;
        
    }

    public static void main(String[] args) {
        SomaNumeros numeros = new SomaNumeros();
        
        numeros.adicionarNumero(3);
        numeros.adicionarNumero(7);
        numeros.adicionarNumero(5);
        numeros.adicionarNumero(10);

        System.out.println("A soma total é = "+ numeros.calcularSoma());

        System.out.println("O maior número é = "+ numeros.encontrarMaiorNumero());

        System.out.println("O menor número é = "+ numeros.encontrarMenorNumero());

        System.out.println("Números adicionados:");
        numeros.exibirNumeros();

        System.out.println("Números na ordem crescente:");
        System.out.println(numeros.ordenarCrescente());

        System.out.println("Números na ordem descrescente:");
        System.out.println(numeros.ordenarDecrescente());

    }
}
