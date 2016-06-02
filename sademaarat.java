//Laadi ohjelma, joka kysyy käyttäjältä seitsemän viikonpäivän sademäärät, jotka se tulostaa näytölle. 
//Käytä ohjelmassasi vakiota ja taulukkoa.

import java.util.Scanner;

public class tehtava2 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		
		final byte paivat = 7;	   
		String[] viikonpaivat;			
		viikonpaivat = new String[paivat];	//taulukon koko
		Short[] sademaara;				
		sademaara = new Short[paivat];		
		
		viikonpaivat[0] = "Maanantai";	//sijoitetaan viikonpäivät taulukkoon
		viikonpaivat[1] = "Tiistai";
		viikonpaivat[2] = "Keskiviiko";
		viikonpaivat[3] = "Torstai";
		viikonpaivat[4] = "Perjantai";
		viikonpaivat[5] = "Lauantai";
		viikonpaivat[6] = "Sunnuntai";
		
		for (int i = 0; i < paivat; i++)	//kysytään sademääriä
		{
			System.out.print("Anna " + viikonpaivat[i] + "n sademäärä(mm): ");
			sademaara[i] = lukija.nextShort();	
		}
		System.out.println("");	
		System.out.println("Kokonaissademäärät ovat");	
		System.out.println("-----------------------");	
		for (int i = 0; i < paivat; i++)	// tulostus
		{
			System.out.println(viikonpaivat[i] + "n sademaara = " + sademaara[i] + " mm");
		}
	}

}
