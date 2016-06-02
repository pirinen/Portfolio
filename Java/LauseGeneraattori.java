import java.util.Scanner;

public class Tehtava3 
{
	//Pääohjelma alkaa
	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		int loop = 1;
		
		do	//Ohjelman loop alkaa
		{
			Generaattori();		//mennää muodostamaan lauseita
			System.out.println("0=lopeta, Muu numero=jatka");
			loop = lukija.nextInt();
		}
		while (loop != 0);	//Ohjelman loop loppuu
		
		System.out.println("Loppu");	//loppu
		
	}	//Pääohjelma loppuu
	
	public static void Generaattori()	//Funktio generoimaan lauseita alkaa
	{
		String sana1, sana2, sana3, sana4, sana5;				//muuttujat
		int r1, r2, r3, r4, r5;									        //muuttujat
		int adPituus, suPituus, prPituus, obPituus, adPituus2;	//muuttujat
		
			//taulut mihin sanoja on tallennettu
		String[] adjektiivi = {"Punainen", "Sininen", "Keltainen", "Tulinen", "Viileä", "Liukas", "Kaareva", "Pyöreä", "Terävä", "Musta"};
		String[] subjekti = {"Ohjelmoija","Kauppias","Kuljettaja","Asentaja","Opettaja","Siivooja","Johtaja","Talonmies","Ompelija","Rokkitähti"};
		String[] predikaatti = {"Syö","Juo","Juoksee","Nukkuu","Kävelee","Soittaa","Lakaisee","Opettaa","Koodaa","Siivoaa"};
		String[] objekti = {"Ruokaa","Autoa","Oppilaita","Kitaraa","Puhelinta","Ohjelmistoa","Taulua","Katua","Lehteä","Vaatetta"};
		String[] adjektiivi2 = {"Punaista", "Sinistä", "Keltaista", "Tulista", "Viileää", "Liukasta", "Kaarevaa", "Pyöreää", "Terävää", "Mustaa"};
			
		r1 = (int)(Math.random() * adjektiivi.length);	//arvotaan satunnainen luku taulun pituuden arvosta
		r2 = (int)(Math.random() * subjekti.length);	//	ja otetaan luku talteen muuttujaan
		r3 = (int)(Math.random() * predikaatti.length);
		r4 = (int)(Math.random() * adjektiivi2.length);
		r5 = (int)(Math.random() * objekti.length);
		
		//edellisen satunnaisen arpomisen luku sijoitetaan taulukon indeksiksi
		//ja tehdään tulostus
		System.out.println(adjektiivi[r1] + " " + subjekti[r2] + " " + predikaatti[r3] +
				" " + adjektiivi2[r4] + " " + objekti[r5]);
		
	}	//Funktio generoimaan lauseita loppuu

}
