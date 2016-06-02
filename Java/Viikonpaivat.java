//ohjelma, joka tallettaa viikonpäivät eri kielillä taulukkoon
//ja tulostaa päivän halutulla kielellä

//import java.io.File;		//luetaan tiedostoa
import java.util.Scanner;

public class Tehtava1 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
											//Suomi = 0, Englanti = 1, Ruotsi = 2
		int kieli, paiva;	
		
		String[][] paivat;				//taulukko päiville
		paivat = new String[7][3];		//taulukon koko
		paivat[0][0] = "Maanantai";	paivat[0][1] = "Monday";	paivat[0][2] = "Måndag";	//asetellaan päiviä taulukkoon
		paivat[1][0] = "Tiistai";	paivat[1][1] = "Tuesday";	paivat[1][2] = "Tisdag";
		paivat[2][0] = "Keskiviikko";paivat[2][1] = "Wednesday";paivat[2][2] = "Onsdag";
		paivat[3][0] = "Torstai";	paivat[3][1] = "Thursday";	paivat[3][2] = "Torsdag";
		paivat[4][0] = "Perjantai";	paivat[4][1] = "Friday";	paivat[4][2] = "Fredag";
		paivat[5][0] = "Lauantai";	paivat[5][1] = "Saturday";	paivat[5][2] = "Lördag";
		paivat[6][0] = "Sunnuntai";	paivat[6][1] = "Sunday";	paivat[6][2] = "Söndag";
		/*
		//Scanneri alkaa
		Scanner lue = new Scanner(new File("‪viikonpaivat.ini"));
		while (lue.hasNextLine())	//luetaan seuraava rivi		
		{
			String rivi = lue.nextLine();	//tallennetaan rivi kerrallaan taulukkoon
			for(int j = 0; j < 3; j++)		//kieli alkaa
			{
				for(int i = 0; i < 7; i++)	//paiva alkaa
				{
					paivat[i][j] = rivi;
				}							//paiva loppuu
			}								//kieli loppuu
		}
		lue.close(); //suljetaan tiedosto
		//Scanneri loppuu
		*/
		System.out.println("Valitse kieli ja haluamasi viikonpäivän numero");					//otsikko
		System.out.print("Millä kielellä haluat tulostuksen(1=Suomi, 2=Englanti, 3=Ruotsi)");	//kielen valinta
		kieli = lukija.nextInt();																//kielen tallennus
		System.out.println("Minkä päivän nimen haluat tietää");									//otsikko
		System.out.print("1=Maanantai, 2=Tiistai, 3=Keskiviikko, 4=Torstai, 5=Perjantai, 6=Lauantai, 7=Sunnuntai");	//päivän valinta
		paiva = lukija.nextInt();																//päivän tallennus
		
		switch (kieli)
		{
		case 1: System.out.print(paiva + ". viikonpäivä on Suomeksi " + paivat[paiva -1][0]);	//case suomi
		break;
		case 2: System.out.print(paiva + ". viikonpäivä on Englanniksi " + paivat[paiva -1][1]);//case englanti
		break;
		case 3: System.out.print(paiva + ". viikonpäivä on Ruotsiksi " + paivat[paiva -1][2]);	//case ruotsi
		break;
		}

	}

}
