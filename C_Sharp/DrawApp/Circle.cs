using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testform
{
    class Circle : Figure
    {
        internal Point end = new Point();
        internal Point begin = new Point();

        public Circle(Pen pen, int x1, int y1, int x2, int y2)
            : base(pen)
        {   //saving points
            begin.X = x1;
            begin.Y = y1;
            end.X = x2;
            end.Y = y2;
        }
        public override void Output(Graphics g)
        {
            g.DrawEllipse(pen, begin.X, begin.Y, end.X - begin.X, end.Y - begin.Y);
                                                                                  
        }

        ~Circle() 
        {

        }
    }
}
