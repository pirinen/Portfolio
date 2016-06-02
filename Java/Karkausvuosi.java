//Karkausvuoden tarkastelua

import java.util.Scanner;

public class Tehtava3 
{

	public static void main(String[] args) 
	{
		//Jukka Pirinen 2.6.2016
		
		Scanner lukija;
		lukija = new Scanner(System.in);
		
		int vuosiluku, paivat = 30; 
		String kk[] = {"Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu",
						"Heinäkuu","Elokuu","Syyskuu","Lokakuu","Marraskuu","Joulukuu"};
		 //^kuukausi taulukko
		
		do							//erisuuri kuin -1 niin loop
		{
			System.out.println("Lopeta syöttämällä -1");//annetaan ohje
			System.out.print("Syötä vuosiluku: ");		//kysytään vuosiluku
			vuosiluku = lukija.nextInt();				//luetaan vuosiluku
			
			if (vuosiluku != -1) 				//jos -1 ei mennä suorittamaan
			{ //if -1 alkaa
			System.out.println("Vuonna " + vuosiluku + " oli kuukausittain päiviä seuraavasti"); //otsikko
			
			for(int i = 0; i < 7; i++)	//loop alkuvuoden tulostusta varten
			{							//koska heinä & elokuussa = 31pv
				if (i % 2 == 0) 		//parilliset kuukaudet
				{
				System.out.println(kk[i] + " " + (paivat + 1));	//31pv
				}
				else					//parittomat kuukaudet
				{				
					if (i == 1)			//helmikuun tarkkailu alkaa
					{
						if (vuosiluku % 4 == 0)	//karkausvuosi
						{	//4. karkausvuosi alkaa
							if (vuosiluku % 100 == 0) 	//EI karkausvuosi
							{	//100. vuosi alkaa
								if(vuosiluku % 400 == 0) //karkausvuosi
								{	//400. alkaa
									System.out.println(kk[i] + " " + (paivat - 1)); //karkausvuosi
								}	//400. loppuu
								else
								{
									System.out.println(kk[i] + " " + (paivat - 2)); //EI karkausvuosi
								}
							}	//100. vuosi loppuu
							else	
							{
								System.out.println(kk[i] + " " + (paivat - 1));	//karkausvuosi
							}
						}	//4. karkausvuosi loppuu	
						else		
						{
						System.out.println(kk[i] + " " + (paivat - 2));	//normaali vuosi
						}	
					}			//helmikuun tarkkailu loppuu	
					else	
					System.out.println(kk[i] + " " + paivat);	//30pv normaalien kuukausien tulostus
				}
			}	//alkuvuoden tulostus loppuu
				//loppuvuoden tulostus alkaa
			for(int i = 7; i < 12; i++)	//loop loppuvuoden tulostusta varten
			{							//koska heinä & elokuussa = 31pv
				if (i % 2 == 0) 		//parilliset kuukaudet
				{
				System.out.println(kk[i] + " " + paivat);
				}
				else			//parittomat kuukaudet
				{
				System.out.println(kk[i] + " " + (paivat + 1));
				}
			}			
				//loppuvuoden tulostus loppuu
			
		}	//if -1 loppuu
		}
		while (vuosiluku != -1);	//erisuuri kuin -1 niin loop
		System.out.println("Loppu");//lopetus
	}

}
