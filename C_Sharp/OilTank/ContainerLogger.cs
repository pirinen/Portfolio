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
        protected bool isLogging = false;
        protected string filename;

        public void StartLogging(string filename)
        {
            isLogging = true;
            this.filename = filename;
                        
        }
       
        public void StopLogging()
        {
            isLogging = false;
        }
        protected void Log()
        {

        }
    }
}
