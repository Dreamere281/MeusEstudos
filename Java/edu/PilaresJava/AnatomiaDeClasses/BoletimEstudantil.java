package edu.PilaresJava.AnatomiaDeClasses;

public class BoletimEstudantil { //Bem Identado
    public static void main(String[] args) {
    	int mediaFinal = 6;
		if (mediaFinal < 6)
			System.out.println("REPROVADO");
		else if (mediaFinal == 6)
			System.out.println("PROVA MINERVA");
		else
			System.out.println("APROVADO");
    }
}
/*arquivo BoletimEstudantil.java  ------ MAl Identado

public class BoletimEstudantil {
public static void main(String[] args) {
int mediaFinal = 6;
if(mediaFinal<6)	
System.out.println("REPROVADO"); 
else if(mediaFinal==6)
System.out.println("PROVA MINERVA"); 
else
System.out.println("APROVADO"); 		
}
}*/