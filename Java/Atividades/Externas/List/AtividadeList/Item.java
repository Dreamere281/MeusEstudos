package Atividades.Externas.List.AtividadeList;

//define uma classe chamada Item. Essa classe representa um item que possui três atributos: nome, preco e quant.
public class Item {
    private String nome;
    private double preco;
    private int quant;

    //Este é o construtor do objeto Item. O construtor é um método especial que é chamado quando um novo objeto da classe é criado.
    public Item(String nome, double preco, int quant){
        this.nome = nome;
        this.preco = preco;
        this.quant = quant;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuant() {
        return quant;
    }

    @Override
    public String toString() {
        return "Item{" +
        "nome='" + nome + '\'' +
        ", preco=" + preco +
        ", quant=" + quant +
        '}';
    }

    
}
