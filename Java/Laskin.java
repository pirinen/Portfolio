//ohjelma, joka toimii erittäin pelkistettynä laskimena

import java.util.Scanner;

public class Tehtava2 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		
		int operaattori;				
		float luku1, luku2, tulos = 0;
		
		System.out.println("Lasketaan kahdella luvulla");	
		System.out.print("Anna ensimmäinen luku: ");	
		luku1 = lukija.nextFloat();						
		System.out.print("Anna toinen luku: ");			
		luku2 = lukija.nextFloat();						
		
		System.out.println("Valitse operaattori jolla lasketaan(1 = yhteenlasku, 2 = vähentäminen, 3 = kertominen, 4 = jakaminen): ");
		operaattori = lukija.nextInt();	//kysytään haluttua lasku tapaa
		
		switch (operaattori)	//mennää switchiin jossa tehdään toimintoja riippuen aiemmasta valinnasta
		{			//1 = Yhteenlasku
		case 1: tulos = luku1 + luku2;
			break;	//2 = Vähennyslasku
		case 2: tulos = luku1 - luku2;
			break;	//3 = Kertolasku
		case 3: tulos = luku1 * luku2;
			break;	//4 = Jakolasku
		case 4: tulos = luku1 / luku2;
			break;
		default: System.out.println("Et valinnut operaattoria oikein"); //jos ei valittu 1-4
			return;	//return että ei tulosta laskennan tulosta mikäli meni valinta väärin
		}	//tähän oli voinut tehdä loopin että olisi palannut aina alkuun laskennan jälkeen
		System.out.println("Laskennan tulos: " + tulos); //tulostetaan lopputulos
				
	}

}
