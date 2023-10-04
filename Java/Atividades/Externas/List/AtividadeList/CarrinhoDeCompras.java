package Atividades.Externas.List.AtividadeList;

import java.util.ArrayList;
import java.util.List;

public class CarrinhoDeCompras {

    //! Esta linha declara um atributo privado chamado itemList do tipo List<Item>. Uma lista que pode conter objetos do tipo Item.
    private List <Item> itemList;

    //! Este é o construtor da classe CarrinhoDeCompras. Neste caso, o construtor inicializa a lista itemList criando uma nova instância de ArrayList, que é uma implementação da interface List. Isso cria uma lista vazia que pode ser usada para armazenar os objetos do tipo Item
    public CarrinhoDeCompras(){
        this.itemList = new ArrayList<>();
    }

    public void adicionarItem(String nome, double preco, int quant){
        //Método construtor do objeto Item
        Item item = new Item(nome, preco, quant);
        //item é uma instância da classe Item 
        this.itemList.add(item);
    }

    public void removerItem(String nome){
        //!uma nova lista chamada removerItens é criada. Esta lista será usada para armazenar os itens que serão removidos posteriormente.
        List<Item> removerItens = new ArrayList<>();
        if (!itemList.isEmpty()) {
            for(Item i: itemList){ //loop for-each
                //Dentro do loop, verifica-se se o nome do item i (i.getNome()) é igual ao nome fornecido como argumento, ignorando a diferença entre maiúsculas e minúsculas
                if(i.getNome().equalsIgnoreCase(nome)){
                    removerItens.add(i);
                }
            }
            itemList.removeAll(removerItens);
        } 
        else {
            System.out.println("O carrinho de compras está vazio");
        }
    }

    public double calcularValorTotal(){
        double valorTotal = 0d;
        if (!itemList.isEmpty()) {
            //Pra cada Item i na lista calcula-se o preço de i pela quantidade utilizando os métodos e adicionando esse valorItem ao valorTotal 
            for(Item i: itemList){
                double valorItem = i.getPreco()*i.getQuant(); 
                valorTotal += valorItem;
            }   
            return valorTotal; 
        } 
        else {
            throw new RuntimeException("Lista vazia!!");
        }
    }

    public void exibirItens(){
        if (!itemList.isEmpty()) {
            System.out.println(this.itemList);
        } 
        else {
            System.out.println("A lista está vazia");           
        }
    }

    @Override
    public String toString() {
        return "CarrinhoDeCompras{" +
        "itens=" + itemList +
        '}';
    }

    public static void main(String[] args) {
        //!Método construtor da classe CarrinhoDeCompras iniciando uma nova instância de ArrayList da linha 12
        CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();
        carrinhoDeCompras.adicionarItem("Lápis", 2d, 3);
        carrinhoDeCompras.adicionarItem("Lápis", 2d, 3);
        carrinhoDeCompras.adicionarItem("Caderno", 35d, 1);
        carrinhoDeCompras.adicionarItem("Borracha", 2d, 2);

        carrinhoDeCompras.removerItem("Lápis");

        carrinhoDeCompras.exibirItens();

        System.out.println("O valor total da compra é = " + carrinhoDeCompras.calcularValorTotal());
    }
    

}
