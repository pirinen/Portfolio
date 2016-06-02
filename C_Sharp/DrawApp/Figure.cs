using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testform
{
    public abstract class Figure
    {
        public Pen pen = new Pen(Color.Blue);       //pen for figures
        public Figure(Pen pen) 
        {
            this.pen = pen; 
        }   

        public abstract void Output(Graphics g);    //output

    }
}
