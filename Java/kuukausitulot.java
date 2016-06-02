//Laadi ohjelma, joka ottaa taulukkoon talteen kahdentoista kuukauden tulot ja laskee sekä tulostaa 
//näytölle tuloista yhteenlasketun vuositulon, keskitulon kuukautta kohti, sekä suurimman kuukausikohtaisen tulon.

import java.text.DecimalFormat;
import java.util.Scanner;

public class Tehtava2 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		
		final int kk = 12;					//kuukausien lkm
		float summa = 0, ka;				//summalle ja keskiarvolle
		int suurin = 0;						//suurimman tulon selvitykseen
		float[] kktulot;					//taulukko kuukausille
		kktulot = new float[kk];
		DecimalFormat desi = new DecimalFormat("###.##"); //kahden desimaalin tarkkuudelle
		
		System.out.println("Syötä kuukausikohtaiset tulot");	//kysytään tulot
		
		for(int i = 0; i < kk; i++)
		{									//tallennetaan tuloja taulukkoon
			System.out.print("Anna " + (i+1) + ". kuukauden tulo: ");
			kktulot[i] = lukija.nextFloat();
		
			summa = summa + kktulot[i];			//lasketaan kokonaissummaa
		}
		
		for (int i = 1; i < kktulot.length; i++)	//selvitetään suurinta tuloa
				{
					if (kktulot[i] > kktulot[suurin])
					{
						suurin = i;
					}
				}		
		
		ka = summa / kk;					//keskiarvon laskeminen
		System.out.println("Kokonaistulot ovat: " + desi.format(summa));
		System.out.println("Keskiarvoinen kuukausitulo on: " + desi.format(ka));
		System.out.println("Suurin kuukausitulo on: " + kktulot[suurin]);
	}	//ja tulostetaan tulokset

}
