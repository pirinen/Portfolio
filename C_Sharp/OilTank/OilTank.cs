using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Container1._0
{ //Jukka Pirinen 2.6.2016
    class OilTank : Container //OilTankille peritään luokka Container
    {
        
        long tunnus;
        Location location;
        
        public OilTank(double capacity, long tunnus, Location location) //muodostin
            : base(capacity)
        {
            
            this.tunnus = tunnus;
            this.location = location;
            
        }
        
        public override void Setamount(double newvalue)
        {
            GetalarmLevel(); //haetaan alarmlevel

            base.Setamount(newvalue); //kirjoitetaan aina tämä

            if (amount < alarmLevel) //kirjoitetaan jos alarmlevel on alle arvon
        
            {

                StartLogging(@"C:\Users\Uusi kansio (2)\alarms.txt");

                if (File.Exists(@"C:\Users\Uusi kansio (2)\alarms.txt")) //jos olemassa
                {
                    StreamWriter sw = File.AppendText(@"C:\Users\Uusi kansio (2)\alarms.txt"); //lisätään tekstiä
                    string timestamp = DateTime.Now.ToString("dd.MM.yyyy hh:mm:ss"); //aika
                    sw.WriteLine(tunnus + " " + timestamp + " " + "amount " + amount); //loput
                    sw.Close();
                }
                else //jos ei ole olemassa
                {
                    StreamWriter sw = File.CreateText(@"C:\Users\Uusi kansio (2)\alarms.txt");
                    string timestamp = DateTime.Now.ToString("dd.MM.yyyy hh:mm:ss");
                    sw.WriteLine(tunnus + " " + timestamp + " " + "amount " + amount);
                    sw.Close();
                }

                StopLogging();

            }   
            
        }

        protected int alarmLevel;

        public int GetalarmLevel()
        {
            alarmLevel = 300;
            return alarmLevel;
        }

        public void SetalarmLevel() //setteri alarmLevel
        {
            alarmLevel = 300;
        }
        ~OilTank() //--------
        {

        }
    }

}
