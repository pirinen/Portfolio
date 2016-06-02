//Anagrammin tarkastelua
import java.util.Arrays;
import java.util.Scanner;

public class Tehtava1 
{
	//Pääohjelma alkaa
	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		String sana1, sana2;
		
		System.out.println("Anagrammin testausohjelma");	//otsikko
		System.out.println("Anna ensimmäinen sana");
		sana1 = lukija.nextLine();
		System.out.println("Anna toinen sana");
		sana2 = lukija.nextLine();
		
		tarkastaAna(sana1, sana2);	//mennään funktioon tarkastamaan anagrammiutta
		
		if (tarkastaAna(sana1, sana2)== true)	//jos oli tosi
		{
			System.out.println(sana1 + " ja " + sana2 + " ovat anagrammeja.");
		}
		else	//jos ei ollut tosi
		{
			System.out.println(sana1 + " ja " + sana2 + " eivät ole anagrammeja.");
		}
		
	}	//Pääohjelma loppuu
	
		//Funktio anagrammin tarkastukseen alkaa
	public static boolean tarkastaAna(String eka, String toka)
	{
		if (eka.length() != toka.length()) {return false;}	//jos sanojen pituudet ovat erisuuria, palautetaan false
		
		char[] taulukko1 = eka.toCharArray();	//tallennetaan sanat taulukoihin
		char[] taulukko2 = toka.toCharArray();
		
		Arrays.sort(taulukko1);					//järjestetään taulukot aakkosjärjestykseen
		Arrays.sort(taulukko2);	
		
		String sana11 = new String(taulukko1);	//tallennetaan taulukot takaisin String muuttujiin
		String sana22 = new String(taulukko2);
		
		return sana11.equals(sana22);			//Ja verrataan ovatko nyt syntyneet sanat samoja

	}	//Funktio anagrammin tarkastukseen loppuu

}
