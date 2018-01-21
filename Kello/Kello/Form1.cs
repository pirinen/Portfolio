using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Threading;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Kello
{
    public partial class Form1 : Form
    {
        Stopwatch stopWatch = new Stopwatch();
        Stopwatch stopWatchTotal = new Stopwatch();
        bool ajastin = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Text = DateTime.Now.ToString("HH:mm:ss");     //Nykyinen aika
            if (ajastin == true)
            {               
                label2.Text = stopWatch.Elapsed.ToString(); //Juokseva aika
            }
        }

        private void StartBtn_Click(object sender, EventArgs e)
        {
            ajastin = true;
            stopWatch.Start();
            stopWatchTotal.Start();
        }

        private void StopBtn_Click(object sender, EventArgs e)
        {
            ajastin = false;
            stopWatch.Stop();
            stopWatchTotal.Stop();
            label2.Text = stopWatch.Elapsed.ToString();
            label3.Text = stopWatchTotal.Elapsed.ToString();
            stopWatch.Reset();  //Nollataan, että saadaan juokseva aika keskelle alkamaan alusta

        }

        private void SaveBtn_Click(object sender, EventArgs e)
        {
            File.AppendAllText("C:\\Users\\pirin\\Omat\\Ohjelmat\\ajat.txt", "Totaltime: " + (stopWatchTotal.Elapsed.ToString() + " - Aika: " + DateTime.Now.ToString("dd.MM.yyyy HH:mm:ss")) + Environment.NewLine);
            MessageBox.Show("Tiedot tallennettu", "Tallennus");
            /*
            using (StreamWriter writer = new StreamWriter("C:\\Users\\pirin\\Omat\\Ohjelmat\\ajat.txt"))
            {
                writer.WriteLine(stopWatchTotal.Elapsed.ToString() + " " + DateTime.Now.ToString("dd.MM.yyyy HH:mm:ss"));
                MessageBox.Show("Tiedot tallennettu","Tallennus");
            }*/
        }

        private void ReStartBtn_Click(object sender, EventArgs e)
        {
            stopWatch.Reset();
            stopWatchTotal.Reset();
            label2.Text = stopWatch.Elapsed.ToString();
            label3.Text = stopWatch.Elapsed.ToString();
        }
    }
}
