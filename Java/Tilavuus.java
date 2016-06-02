//ohjelma, joka laskee ympyrän pinta-alan tai pallon tilavuuden

import java.text.DecimalFormat;
import java.util.Scanner;

public class Tehtava1 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		
		int luku;
		double sade,tulos;	//pitää olla double, ei muuten hyväksy tuota Math.PI
		DecimalFormat desi = new DecimalFormat("###.##"); //kahden desimaalin tarkkuudelle
		
		System.out.println("Haluatko laskea pallon tilavuuden vai ympyrän pinta-alan?");
		System.out.println("Valitse 1=pallo tai 2=ympyrä");	//kysytään kumpaa lasketaan
		luku = lukija.nextInt();							//luetaan tulos muuttujaan
			//ja mennään valinnasta riippuen laskemaan tulosta
		if (luku == 1)	//pallon tilavuus
		{
			System.out.println("Anna pallon säde");	//kysytään pallon sädettä
			sade = lukija.nextFloat();				      //luetaan muuttujaan
			tulos = (4*Math.PI*(sade*sade*sade))/3;	//lasketaan pallon tilavuus
			System.out.println("Pallon tilavuus säteellä " + desi.format(sade) + " on: " + desi.format(tulos));
		}	//^tulostetaan lopputulos
		if (luku == 2)	//ympyrän pinta-ala
		{
			System.out.println("Anna ympyrän säde");	//kysytään ympyrän sädetta
			sade = lukija.nextFloat();					      //luetaan muuttujaan
			tulos = Math.PI * (sade * sade);			    //lasketaan ympyrän pinta-ala
			System.out.println("Ympyrän pinta-ala säteellä " + desi.format(sade) + " on: " + desi.format(tulos));
		}	//^tulostetaan lopputulos
		
	}

}
