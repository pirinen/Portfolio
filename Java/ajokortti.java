//Laadi ohjelma, joka kysyy käyttäjältä kuvitteellisen henkilön seuraavat tiedot: ikä, pituus metreinä, paino 
//sekä tieto siitä, omistaako kyseinen henkilö ajokortin. Valitse tarvittavien muuttujien tietotyypit siten, 
//että ne vievät mahdollisimman vähän turhaa tilaa. Kun olet kysynyt tiedot käyttäjältä, tulosta ne näytölle.


import java.util.InputMismatchException;
import java.util.Scanner;

public class tehtava1 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen
	
		short ika, paino;	
		float pituus;		
		char ajokortti;		//k tai e
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		try								//virheellistä syöttöä varten
		{
			System.out.print("Syota ikasi: ");	//kysytään ika
			ika = lukija.nextShort();			      //luetaan ika
			System.out.print("Syota pituutesi(muoto 0,0)metreina: ");
			pituus = lukija.nextFloat();	      //luetaan pituus
			System.out.print("Syota painosi (kg): ");	//kysytään paino
			paino = lukija.nextShort();					//luetaan paino
		
			do	//loop jos käyttäjä ei osaa syöttää pientä k tai e
			{
				System.out.print("Onko sinulla ajokorttia(k/e): "); //onko korttia
				ajokortti = lukija.next().charAt(0);	              //luetaan tulos
			}
			while (ajokortti != 'k' && ajokortti != 'e');	        //loop kunnes k tai e
			// tulostukset
			System.out.println("Ikasi on: " + ika + " vuotta");
			System.out.println("Pituutesi on: " + pituus + "m");
			System.out.println("Painosi on : " + paino + "kg");
			// if lauseella kortin omistajuuden tulostus
			if (ajokortti == 'k')
			{
				System.out.println("Sinulla on ajokortti");
			}
			else
			{
				System.out.println("Sinulla ei ole ajokorttia");
			}
		}	  //napataan kiinni virheestä
		catch (InputMismatchException e)
		{	  //annetaan virheilmoitus
			System.out.println("Syötit virheellisen arvon");
			System.exit(0); //lopetetaan ohjelma
		}
	}

}
