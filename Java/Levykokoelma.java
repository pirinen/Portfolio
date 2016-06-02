//Levykokoelma

import java.util.Iterator;
import java.util.Scanner;
import java.util.Vector;
	//Jukka Pirinen 2.6.2016  //Pääohjelma
public class Tehtävä1 
{
	
	public static void main(String[] args) //pääohjelma alkaa
	{		
		Scanner lukija;
		lukija = new Scanner(System.in);
		int loop;	//pääloopille

		Levykokoelma kokoelma = new Levykokoelma();	//luodaan uusi levykokoelma
		
		do	//Pääohjelman loop alkaa
		{
			System.out.println("Levykokoelman hallinta");		//otsikko
			System.out.println("0=Lopeta, 1=lisää levy, 2=poista levy, 3=tulosta kokoelma");
			loop = lukija.nextInt();	//annetaan vaihtoehdot ja luetaan talteen 
			
			switch (loop)	//switch case valinnoille alkaa
			{			
			case 1: kokoelma.LisaaLevy();
				break;
			case 2: kokoelma.PoistaLevy();
				break;
			case 3: kokoelma.TulostaKokoelma();
				break;
			}	//switch case valinnoille loppuu
		}
		while (loop != 0);	//Pääohjelman loop loppuu
		System.out.println("Ohjelma lopetetaan");	//loppu

	}	//pääohjelma loppuu
	
}

	/****************************************************************************************/
import java.util.Scanner;

public class Cdlevy		//Luokka cd-levylle alkaa
	{
		Scanner lukija = new Scanner(System.in);
		protected String artisti, levynNimi;
		protected int vuosi;	//muuttujat
		
			//Setterit alkaa
		public void setArtisti(String uusiArtisti) {artisti = uusiArtisti;}
		public void setLevynNimi(String uusilevynNimi) {levynNimi = uusilevynNimi;}
		public void setVuosi(int uusiVuosi) {vuosi = uusiVuosi;}
			//Setterit loppuu
			//Getterit alkaa
		public String getArtisti() {return artisti;}
		public String getLevynNimi() {return levynNimi;}
		public int getVuosi() {return vuosi;}
			//Getterit loppuu
		
		public void AnnaTiedot()	//Kysytään käyttäjältä levyn tietoja alkaa
		{
			System.out.println("Anna artistin nimi:");
			setArtisti(lukija.nextLine());
			System.out.println("Anna levyn nimi:");
			setLevynNimi(lukija.nextLine());
			System.out.println("Anna levyn julkaisuvuosi:");
			setVuosi(lukija.nextInt());
		}	//Kysytään käyttäjältä levyn tietoja loppuu
		
		public void TulostaTiedot()	//Levyn tietojen tulostus alkaa
		{
			System.out.println("Artistin nimi: " + getArtisti());
			System.out.println("Levyn nimi: " + getLevynNimi());
			System.out.println("Julkaisuvuosi: " + getVuosi());
		}	//Levyn tietojen tulostus loppuu
		
	}	//Luokka cd-levylle Loppuu

	/****************************************************************************************/
	import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Levykokoelma	//Luokka levykokoelma alkaa
	{
		Scanner lukija = new Scanner(System.in);
		ArrayList<Object> levynTallennus = new ArrayList<Object>();	//levyjen tallennus ArrayListiin

		//public Levykokoelma() {}
		
		public void LisaaLevy()	//Uuden levyn lisäys kokoelmaan alkaa
		{	
			Cdlevy uusiCd = new Cdlevy();		//tehdään uusi levy
			uusiCd.AnnaTiedot();				//kysytään levyn tietoja käyttäjältä
			uusiCd.TulostaTiedot();				//tulostetaan edellä mainitut tiedot
			levynTallennus.add(uusiCd.artisti + "; " + uusiCd.levynNimi + ", " + uusiCd.vuosi);	//laitetaan listaan uuden levyn tiedot
			System.out.println("Uuden levyn tiedot tallennettu!");	//ilmoitetaan käyttäjälle tietojen tallentamisesta
			
		}	//Uuden levyn lisäys kokoelmaan loppuu
		
		public void PoistaLevy()	//Levyn poistaminen kokoelmasta alkaa
		{
			int levynnro;
			
			System.out.println("Anna levyn numero jonka haluat poistaa:");	//ohje käyttäjälle
			levynnro = lukija.nextInt();
			levynTallennus.remove(levynnro-1);	//-1 ettei käyttäjän tarvitse huomioida 0-indeksiä taulukossa
			
		}	//Levyn poistaminen kokoelmasta loppuu
		
		public void TulostaKokoelma()	//Kokoelman tulostus alkaa
		{
			int i = 0;	//levyn järjestysnro, joka lisätään jokaisen tulostuksen yhteydessä
			
			System.out.println("Levykokoelma");		//otsikko
			System.out.println("Levyjen tiedot");	//otsikko
			
			Iterator<Object> iteraattori = levynTallennus.iterator();	//iteraattori
			while (iteraattori.hasNext())			//käydään läpi niin pitkään kuin tavaraa riittää
			{
				i++;	//tallennettujen levyjen järjestysnumero varten, helpottaa poistamista
				String tulostus = (String)iteraattori.next();			
				System.out.println("Levy nro: " + i + " " + tulostus);
			}	//iteraattori loppuu
			System.out.println("-----------------");	//välin tulostus
			
		}	//Kokoelman tulostus alkaa
		
	}	//Luokka levykokoelma loppuu

	
