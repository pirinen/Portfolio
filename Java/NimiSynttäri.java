//funktioiden yhdistelyä
import java.util.Scanner;

public class Tehtava2 
{	 //Jukka Pirinen 2.6.2016
	
	static Scanner lukija = new Scanner(System.in);
	
		public static void main(String[] args)	//Pääohjelma alkaa
		{
			StringBuffer nimi = new StringBuffer();	//StringBuffer muuttuja nimi
			nimi.append("Nimesi on " + Nimi("") + " ja syntymäaikasi: " + SyntymaAika(""));	//lisätään nimeen tavaraa
			System.out.println(nimi);	//tulostetaan nimi
			
		}	//Pääohjelma loppuu
		
		public static String Nimi(String nimi)	//Nimi funktio alkaa
		{
			System.out.println("Kirjoita nimesi: ");	//kysytään
			nimi = lukija.nextLine();					//luetaan
			return nimi;								//palautetaan
		}	//Nimi funktio loppuu
		
		public static String SyntymaAika(String aika)	//SyntymäAika funktio alkaa
		{
			System.out.println("Kirjoita syntymäaikasi: ");	//kysytään
			aika = lukija.nextLine();						//luetaan
			return aika;									//palautetaan
		}	//SyntymäAika funktio loppuu
}
