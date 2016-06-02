using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testform
{
    class Drawing : List<Figure>
    {
        public void Output(Graphics g) 
        {
            foreach (Figure fig in this)
            {
                fig.Output(g);
            }
        }
        public void Serialize(StreamWriter s)   //saving drawings
        {
            s.WriteLine("Drawing tallennus");
        }
    }
}
