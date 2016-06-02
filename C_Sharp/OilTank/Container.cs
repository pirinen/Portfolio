using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Container1._0
{ //Jukka Pirinen 2.6.2016

    partial class Container 
    {
        
        public double capacity, amount;
        public const double maximumLevel = 1.0, minimumLevel = 0.0;

        public Container(double initialCapacity) //muodostin Container
        {
            capacity = initialCapacity;
            amount = 0.0;
        }
        ~Container() //tuhooja Container
        {

        }
        public double GetCapacity() //capacityn accessor-funktio
        {
            return capacity;
        }
        public double Getamount() //amountin accessor
        {
            return amount;
        }
        public virtual void Setamount(double newvalue) //amountin setteri
        { 
          
            if (File.Exists(@"C:\Users\Uusi kansio (2)\filename.txt")) //jos olemassa
            {
                StreamWriter sw = File.AppendText(@"C:\Users\Uusi kansio (2)\filename.txt"); //lisätään tekstiä
                string timestamp = DateTime.Now.ToString("dd.MM.yyyy hh:mm:ss"); //aika
                sw.WriteLine(timestamp + "; " + GetFillLevel() + "%"); //loput
                sw.Close();
            }
            else //jos ei ole olemassa
            {
                StreamWriter sw = File.CreateText(@"C:\Users\Uusi kansio (2)\filename.txt");
                string timestamp = DateTime.Now.ToString("dd.MM.yyyy hh:mm:ss");
                sw.WriteLine(timestamp + "; " + GetFillLevel() + "%");
                sw.Close();
            }
        }
        public double GetFillLevel() //täyttöaste
        {
            return amount / capacity * 100; //prosentit
        }

        public void AskInfo()
        {
            do //toistetaan kunnes arvot on välillä 0-2000
            {
                Console.WriteLine("Amount: ");
                amount = double.Parse(Console.ReadLine());
                
                    try 
                {
                    if (amount > capacity || amount < 0)
                        if (amount > capacity)
                            throw new Exception("Amount oli yli 2000! ");
                        else
                            throw new Exception("Amount oli alle 0");
                }
                    catch (Exception teksti)
                    {
                        Console.WriteLine(teksti.ToString());
                    }

            }
            while (amount > capacity || amount < 0); //looppi jos arvot ei osu
        }

        public void PrintSummary()
        {
            
           Console.WriteLine("amount " + amount + " litraa");
           Console.WriteLine("Fill level: " + GetFillLevel() + "%");

        }


    }
}
