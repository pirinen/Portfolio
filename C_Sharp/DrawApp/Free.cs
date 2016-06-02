using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testform
{
    class Free : Figure
    {
        internal Point end = new Point();
        internal Point start = new Point();
        
        public Free(Pen pen, Point start1, Point end1 )
            :base (pen)
        {
            start = start1;
            end = end1;
        }

        public override void Output(Graphics g)
        {
            g.DrawLine(pen, start, end);
        }
        
    }
}
