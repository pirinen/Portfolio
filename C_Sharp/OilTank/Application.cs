using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Container1._0
{ //Jukka Pirinen 2.6.2016
    class Application
    {
        public void Run()
        {
            string sana;

            OilTank sailio = new OilTank(2000, 12345, new Location(62.0000, 32.0000, 2.0));
            sailio.StartLogging(@"C:\Users\Uusi kansio (2)\filename.txt"); //tiedostonsijainti
            
            do //pääsilmukka
            {
                Console.WriteLine("Syötä lopeta jos haluat lopettaa");
                sana = Console.ReadLine();

                if (sana != "lopeta")
                {
                    
                    sailio.AskInfo(); 
                    sailio.Setamount(0); 
                   // sailio.SetAmount(0); //errorlog, tämä jäi nyt pois virtualin myötä
                    sailio.GetFillLevel();
                    sailio.PrintSummary();
                    
                }
            }
            while (sana != "lopeta");
            sailio.StopLogging(); //loggauksen lopetus

            Console.ReadLine();
        }
    }
}
