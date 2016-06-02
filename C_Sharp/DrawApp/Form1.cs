using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Testform
{
    public partial class Form1 : Form
    {
        public int x1, y1, x2, y2, x3, y3;                         
        //Point currentPoint;                                                    
        Drawing p = new Drawing();                          
        Figure currentfig; 
        
        Graphics g; 
        Pen currentPen = new Pen(Color.Black, 1);       //currentpen
        Point start = new Point(0,0);                   //start point
        Point end = new Point(0,0);                     //end point
        Point kolmas = new Point(0,0);                  //Triangle point
        bool drawing = false; 
       
        public Form1()                                      //komponentin tila                                                            // public int state = LINE;
        {
            InitializeComponent();                  
        }
        private void panel1_MouseDown(object sender, MouseEventArgs e)  //mouseclick
        {
            x1 = e.X;                               //location X
            y1 = e.Y;                               //location Y

            start = e.Location;                     //location x & y

            if (e.Button == MouseButtons.Left)      //left btn down
            {                   
                drawing = true;
                                     
                if (lineToolStripMenuItem.Checked)      //Line on mousemove
                {
                    currentfig = new Line(new Pen(currentPen.Color, currentPen.Width), x1,y1,x1,y1);
                }                                       //End line
                if (circleToolStripMenuItem.Checked)    //Circle on mousemove
                {
                    currentfig = new Circle(new Pen(currentPen.Color, currentPen.Width), x1,y1,x1,x1);
                }                                       //End circle
                if (squareToolStripMenuItem.Checked)    //Square on mousemove
                {
                    currentfig = new Square(new Pen(currentPen.Color, currentPen.Width), x1,y1,x1,x1);
                }                                       //End square
            }
            if (e.Button == MouseButtons.Right)         //right btn down
            {
                kolmas = e.Location;                    //Triangle point on location
            }
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)  //Mousemove
        {
            x3 = e.X;                               //location X
            y3 = e.Y;                               //location Y
                    //currentPoint = e.Location;            
            if (drawing)                            //if drawing true
            {                                       //Mouse leftBTN down
                if (freeToolStripMenuItem.Checked)          //Drawing free on mouse move
                {          
                    end = e.Location;                       //end point location
            
                    p.Add(new Free(new Pen(currentPen.Color, currentPen.Width), start, end));
                    p.Output(panel1.CreateGraphics());      //draw
                }                                           //End free draw

                if (lineToolStripMenuItem.Checked)          //Drawing line on mouse move                
                {   
                    Refresh();
                    if (currentfig != null)                             
                    {
                        ((Line)currentfig).end.X = x3;                  
                        ((Line)currentfig).end.Y = y3;                  
                        currentfig.Output(panel1.CreateGraphics());     
                    }
                }                                           //End drawing line

                if (circleToolStripMenuItem.Checked)        //Drawing circle on mouse move
                {
                    Refresh();
                    if (currentfig != null)
                    {
                        ((Circle)currentfig).end.X = x3;
                        ((Circle)currentfig).end.Y = y3;
                        currentfig.Output(panel1.CreateGraphics());
                    }
                }                                           //End drawing circle

                if (squareToolStripMenuItem.Checked)        //Drawing square on mouse move
                {
                    Refresh();
                    if (currentfig != null)
                    {
                        ((Square)currentfig).end.X = x3;
                        ((Square)currentfig).end.Y = y3;
                        currentfig.Output(panel1.CreateGraphics());
                    }
                }                                           //End drawing square
            }                               
            end.X = e.X;                                    //point for triangle
            end.Y = e.Y;                                    //point for triangle
            start = end;                                    //Free drawing start, end
                        
        }                                                   //Mousemove ends

        private void panel1_MouseUp(object sender, MouseEventArgs e)    //mousebtn up
        {
            x2 = e.X;                                       //location x
            y2 = e.Y;                                       //location y
            
            drawing = false;                                
           
            if (e.Button == MouseButtons.Left)              //left btn down
            {
                if (lineToolStripMenuItem.Checked)          //line           
                    p.Add(new Line(new Pen(currentPen.Color, currentPen.Width), x1, y1, x2, y2));
                p.Output(panel1.CreateGraphics());          //drawline

                if (circleToolStripMenuItem.Checked)        //circle
                    p.Add(new Circle(new Pen(currentPen.Color, currentPen.Width), x1, y1, e.X, e.Y));
                p.Output(panel1.CreateGraphics());          //drawcircle
                
                if (squareToolStripMenuItem.Checked)        //square
                    p.Add(new Square(new Pen(currentPen.Color, currentPen.Width), x1, y1, e.X, e.Y));
                p.Output(panel1.CreateGraphics());          //drawsquare

                if (kolmioToolStripMenuItem.Checked)        //triangle
                    p.Add(new Triangle(new Pen(currentPen.Color, currentPen.Width), x1, y1, end, kolmas ));
                    p.Output(panel1.CreateGraphics());      //drawtriangle
            }            
        }                                                               //mousebtn ends

        private void panel1_Paint(object sender, PaintEventArgs e)  //drawing panel
        {            
            p.Output(panel1.CreateGraphics());                      //p = drawing
        }                                                           //drawing panel end

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)   //app infobox
        {
            MessageBox.Show("Tietoja sovelluksesta...", "About drawing app");
        }                                                                       //app infobox ends

        private void openToolStripMenuItem_Click(object sender, EventArgs e)    //open new file
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            DialogResult result = openFileDialog.ShowDialog();
        }                                                                       //open new file ends

        private void button1_Click(object sender, EventArgs e)                  //change color btn
        {                                               
            DialogResult r = colorDialog1.ShowDialog(); 
            if (r == DialogResult.OK)                   
            {                                           
                currentPen.Color = colorDialog1.Color;                          //currentpen color
                button1.BackColor = this.colorDialog1.Color;                    //color button color                
            }                                           
        }                                                                       //change color btn ends

        private void PensizeBar_Scroll(object sender, EventArgs e)              //pen size bar
        {
         
            currentPen.Width = PensizeBar.Value;                        //pen size
            label1.Text = "" + PensizeBar.Value;                        //pen size by text
        }                                                                       //pen size bar ends
        
        private void newToolStripMenuItem_Click(object sender, EventArgs e)     //new panel
        {
            g = panel1.CreateGraphics();
            g.Clear(Color.White);                                       //draw empty panel
            p.Clear();                                                  //clear figure list
        }                                                                       //new panel ends


        private void saveToolStripMenuItem_Click(object sender, EventArgs e)        //save button
        {
            Stream myStream;

            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "drw files (*.drw)|*.drw|All files (*.*)|*.*";
            saveFileDialog.RestoreDirectory = true;
            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                if ((myStream = saveFileDialog.OpenFile()) != null)
                {
                    StreamWriter sw = new StreamWriter(myStream);

                    p.Serialize(sw);
                    sw.Close();
                }
            }
        }                                                                           //save button ends
        // Uncheck other toolstrip menu items
        private void circleToolStripMenuItem_Click(object sender, EventArgs e)  //circle checked
        {
            UncheckOtherToolStripMenuItems((ToolStripMenuItem)sender);          //uncheck other
        }                                                                       

        private void lineToolStripMenuItem_Click(object sender, EventArgs e)    //line checked
        {
            UncheckOtherToolStripMenuItems((ToolStripMenuItem)sender);
        }

        private void squareToolStripMenuItem_Click(object sender, EventArgs e)  //square checked
        {
            UncheckOtherToolStripMenuItems((ToolStripMenuItem)sender);
        }

        private void freeToolStripMenuItem_Click(object sender, EventArgs e)    //free drawing checked
        {
            UncheckOtherToolStripMenuItems((ToolStripMenuItem)sender);
        }

        private void kolmioToolStripMenuItem_Click(object sender, EventArgs e)  //triangle checked
        {
            UncheckOtherToolStripMenuItems((ToolStripMenuItem)sender); 
        }
        // Uncheck other toolstrip menu items ends
        private void quitToolStripMenuItem_Click(object sender, EventArgs e)    //quit btn
        {
            Close();                                                    //close program
        }                                                                       //quit btn ends

        public void UncheckOtherToolStripMenuItems(ToolStripMenuItem selectedMenuItem)
        {                                               //unchecking other toolstrip menu items
            selectedMenuItem.Checked = true;
            foreach (var ltoolStripMenuItem in (from object
                                                item in selectedMenuItem.Owner.Items
                                                let ltoolStripMenuItem = item as ToolStripMenuItem
                                                where ltoolStripMenuItem != null
                                                where !item.Equals(selectedMenuItem)
                                                select ltoolStripMenuItem))
                (ltoolStripMenuItem).Checked = false;

            selectedMenuItem.Owner.Show();      //leave menu item open
        }                                               //unchecking other toolstrip menu items ends
        
    }
}
