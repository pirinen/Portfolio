using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testform
{
    class Triangle : Figure
    {
        internal Point end = new Point();
        internal Point begin = new Point();
        Point kolmas = new Point(0);
        public Triangle(Pen pen, int x, int y, Point kolmas1, Point end1)
            : base(pen)
        {
            end = end1;
            begin.X = x;
            begin.Y = y;
            kolmas = kolmas1;
        }
        public override void Output(Graphics g)
        {
            Point[] pointti = { begin, end, kolmas };
            g.DrawPolygon(pen, pointti);

        }
    }
}
