using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Container1._0
{ //Jukka Pirinen 2.6.2016
    class Location
    {
        public double latitude, longitude, elevation; //leveys, pituus, korkeus 

        public Location(double latitude, double longitude, double elevation) //muodostin
        {
            this.latitude = latitude;
            this.longitude = longitude;
            this.elevation = elevation;
        }
        ~Location() //tuhooja
        {

        }
    }
}

