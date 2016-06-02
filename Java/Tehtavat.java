import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
	//Jukka Pirinen 2.6.2016		//Tehtävä 2, pääohjelma
public class Tehtävä2 
{

	public static void main(String[] args) 	//Pääohjelma alkaa
	{
		
		Scanner lukija = new Scanner(System.in);
		int loop;
		
		tehtavat uusitehtava = new tehtavat();
		Queue<String> jono = new LinkedList<String>();	//tehdään uusi jono
		
		do
		{
			System.out.println("0=Lopeta, 1=Lisää uusi tehtävä, 2=Tulosta ja poista tehtävät");		//Otsikot ja ohjeet
			System.out.println("3=Tulosta tehtävät, 4=Poista kaikki tehtävät, 5=Poista ensimmäinen");
			loop = lukija.nextInt();
			int  i = 0;		//tehtävälaskuri
			switch (loop)
			{
			case 1:	jono.offer(uusitehtava.AnnaKuvaus());		//lisätään jonoon tehtava
					uusitehtava.TulostaKuvaus();				//tulostetaan vielä käyttäjän antama syötä
					System.out.println("; tallennettu jonoon");	//ja ilmoitetaan se tallennetuksi
				break;
				
			case 2: while(jono.peek() != null)	//kunnes jono tyhjenee
					{	
						i++;	//tehtävälaskuri
						String tulosta = jono.poll();	//poll hakee ja poistaa alkion jonosta
						System.out.println("Tehtävä:" + i + ", " + tulosta);
					}
				break;
				
			case 3:	for(String lista : jono) 	//tällä ei tehtävät poistu jonosta
					{
						i++;	//tehtävälaskuri
						System.out.println("Tehtävä: " + i + ", " + lista.toString());
					}
					break;
					
			case 4: jono.removeAll(jono);		//poistetaan kaikki jonosta
					System.out.println("Kaikki tehtävät poistettu!");
				break;
				
			case 5:	jono.remove();	//poistaa ensimmäisen jonosta
					System.out.println("Ensimmäinen tehtävä poistettu");
				break;
			}
			System.out.println();	//tyhjä rivi
		}
		while (loop != 0);	//Pääohjelman loop loppuu

		System.out.println("Loppu");
	}	//Pääohjelma loppuu
}
/***********************************************************************************/
//import java.util.Iterator;
//import java.util.Scanner;
	//Jukka Pirinen 1500912		//Tehtävä 2, tehtavat luokka
class tehtavat	//Tehtävät luokka alkaa
{
	Scanner lukija = new Scanner(System.in);
	protected String kuvaus;	//merkkijono tehtävän kuvaukselle
	
	public tehtavat(){}
		//Setteri
	public void setKuvaus(String uusiKuvaus) {kuvaus = uusiKuvaus;}
	public String getKuvaus() {return kuvaus;}
		//Getteri
	public String AnnaKuvaus()	//kysytään tehtävän kuvausta alkaa
	{
		System.out.println("Anna tehtävän kuvaus");
		setKuvaus(lukija.nextLine());
		return kuvaus;
	}	//kysytään tehtävän kuvausta loppuu
	
	public void TulostaKuvaus()	//tulostus alkaa
	{
		System.out.print("Tehtävä: " + getKuvaus());
	}	//tulostus loppuu
	
}	//Tehtävät luokka loppuu
