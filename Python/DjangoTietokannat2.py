from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.template.loader import get_template
from django.template import Context
from random import randint
from django import template
from django.http import HttpResponseRedirect
from setuptools.depends import Require
from datetime import datetime, timedelta
import tkinter
import psycopg2

  #Jukka Pirinen    8.9.2016
  #Urheilusuorituksia tietokantaan Djangolla
  #views.py tiedostot
                                                #Viela keskenerainen
  #Html tiedostot alla kommenteissa

class Suorituss(object):

    HenkiloNimiID = "?"
    Nimi = "?"
    Salasana = "?"
    
    LajiLajiID = "?"
    Laji = "?"
    SuoritusID = "?"
    SuoritusLajiID = "?"
    SuoritusNimiID = "?"
    PVM = "?"
    SuoritusAika = "?"

    def __init__(self, HenkiloNimiID, Nimi, Salasana,LajiLajiID,Laji,SuoritusID,SuoritusLajiID,SuoritusNimiID,PVM,SuoritusAika):

        self.HenkiloNimiID = HenkiloNimiID
        self.Nimi = Nimi
        self.Salasana = Salasana
        
        self.LajiLajiID = LajiLajiID
        self.Laji = Laji
        self.SuoritusID = SuoritusID
        self.SuoritusLajiID = SuoritusLajiID
        self.SuoritusNimiID = SuoritusNimiID
        self.PVM = PVM
        self.SuoritusAika = SuoritusAika
            #Suorituss Class loppuu---
            
def VieKantaan(request):    #Tietokantaan vienti

    NimiID = 2  #Joku laskuri pitaisi olla naille ID kentille
    Nimi = "Jukka"#request.GET['nimi']    #ei nyt hae tuolta kirjautumisesta...?!
    Salasana = "Salasana"#request.GET['salasana']
    
    Laji = request.GET['Laji']
    LajiID = 2
    
    Suoritus =  request.GET['Suoritus']
    SuoritusID = 2
    PVM = request.GET['pvm']
    SuoritusAika = request.GET['Suoritusaika']
        #^Muuttujat talteen^
    conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
    print ("Opened database successfully")
    cur = conn.cursor()    #Paa-olio
    
    cur.execute("INSERT INTO Henkilo (NimiID,Nimi,Salasana) \
                VALUES (%s,%s,%s);",(NimiID,Nimi,Salasana));
    cur.execute("INSERT INTO Laji (LajiID,Laji) \
                VALUES (%s,%s);",(LajiID,Laji));
    cur.execute("INSERT INTO Suoritus (SuoritusID,LajiID,NimiID,PVM,SuoritusAika) \
                VALUES (%s,%s,%s,%s,%s);",(SuoritusID,LajiID,NimiID,PVM,SuoritusAika));
    conn.commit()
    return TehtKymppiLogged(request)
                            #Tietokantaan vienti loppuu
                            
def Yhteenveto(request):    #Yhteenveto
        #Tietokantayhteys alkaa
    conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
    print ("Opened database successfully")
    cur = conn.cursor()    #Paa-olio
    cur.execute("SELECT Henkilo.NimiID, Nimi, Salasana,Laji.LajiID,Laji,SuoritusID,Suoritus.LajiID,Suoritus.NimiID,PVM,SuoritusAika from Henkilo, Laji, Suoritus")
    rows = cur.fetchall()
    Suoritukset = []   #Suoritukset lista
    for row in rows:
        h2 = Suorituss(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])    #lisaillaan riveja muuttujaan
        Suoritukset.append(h2)             #sijoitetaan muuttujat listaan
        print(row)      #testitulostus
    t = get_template('Yhteenveto.html')
    lm = t.render(Context({'Suoritukset' : Suoritukset}))
    return HttpResponse(lm)

                            #Yhteenveto loppuu
def UusiHarjoitus(request):     #Uuden harjoituksen lisays

    if request.method == 'POST':

        form = NimiForm(request.POST)
    else:
        form = NimiForm()

    return render(request, 'Uusiharj.html', {'form': form}) #Tullaan TehtKymppiLogged ja tehdaan Uusiharj.html
    
def TehtKymppiLogged(request):  #Tullaan TehtKymppiTuloksesta

    if request.method == 'POST':

        form = NimiForm(request.POST)
    else:
        form = NimiForm()

    return render(request, 'teht10Logged.html', {'form': form}) #Tullaan TehtKymppiTulos ja tehdaan Logged.html
    
def TehtKymppiTulos(request):   #Teht10.html ohjaa tanne

    
    nimi = request.GET['nimi']
    salasana = request.GET['salasana']
    ###nim = template.Context({"nim" : nimi})  #yritys siirtaa nimi uudelle sivulle, ei toimi viela
    ###onnistui = template.Template("Tervetuloa palveluun {{nim}}")
    if nimi == "Jukka" and salasana == "testi":
        return HttpResponseRedirect("http://127.0.0.1:8000/TehtKymppiLogged")   #Kirjautuminen onnistui
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/TehtKymppi")         #Kirjautuminen ei onnistunut


def TehtKymppi(request):    #Aloitus
    if request.method == 'POST':

        form = NimiForm(request.POST)
    else:
        form = NimiForm()

    return render(request, 'teht10.html', {'form': form})   #Aloitussivun formin
    
      #HTML-sivut alkaa
  ##########################

<!doctype html>
<HTML>
	<head>
	
	<TITLE>Teht10</TITLE>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<style>

</style>
	</head>
	<BODY>

	<ul>
	<h2><b> Harjoitusten yhteenveto <b/></h2>
	{% for suorituss in Suoritukset %}
    <li>{{ suorituss.NimiID }}, {{suorituss.Nimi}},{{ suorituss.Salasana }},
	{{ suorituss.LajiID }},{{ suorituss.Laji }},{{ suorituss.SuoritusID }},
	{{ suorituss.LajiID }},{{ suorituss.NimiID }},{{ suorituss.PVM }}
	{{ suorituss.SuoritusAika }}</li>
	{% endfor %}
	<br><br>
  <li><a href="http://127.0.0.1:8000/UusiHarjoitus">Uusi harjoitus</a></li>
  <li><a href="http://127.0.0.1:8000/TehtKymppiLogged">Etusivulle</a></li>
  <li><a href="#tietoja">Tietoja</a></li>

  
	</ul>
	<br>
	</BODY>
</HTML>
  #####################
<!doctype html>
<HTML>
	<head>
	
	<TITLE>Teht10</TITLE>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<style>

</style>
	</head>
	<BODY>
	<form name="Uusiharj" action="http://127.0.0.1:8000/VieKantaan" method="get"; >

	<br>	
	<ul>
	<h2><b> Lisää uusi harjoitus <b/></h2>
	
	Kirjoita uuden harjoituksen tiedot <br>
	<br>
	Laji: <br>
	<input type="text" name="Laji" value="" required><br> <!--required pakottaa laittaamaan arvon tuohon kenttaan -->
	Suoritus: <br>
	<input type="text" name ="Suoritus" value="" required><br>
	Päivämäärä: <br>
	<input type="text" name ="pvm" value="" required><br>
	Suoritusaika: <br>
	<input type="text" name ="Suoritusaika" value="" required><br>
	<br>
	
  <li><a href="http://127.0.0.1:8000/Yhteenveto">Yhteenveto</a></li>
  <li><a href="http://127.0.0.1:8000/TehtKymppiLogged">Etusivulle</a></li>
  <br>
  Lisää uusi harjoitus tietokantaan
  <br>
  	<button onclick="http://127.0.0.1:8000/VieKantaan">Lisää</button>

	</form>
	
	</ul>
	<br>
	</BODY>
</HTML>
  #######################
<!doctype html>
<HTML>
	<head>
	
	<TITLE>Teht10</TITLE>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<style>

</style>
	</head>
	<BODY>
	
	<ul>
	<h2><b> Harjoitusten kirjanpito <b/></h2>	
  <li><a href="http://127.0.0.1:8000/UusiHarjoitus">Uusi harjoitus</a></li>
  <li><a href="http://127.0.0.1:8000/Yhteenveto">Yhteenveto</a></li>
  <li><a href="#tietoja">Tietoja</a></li>

  
	</ul>
	<br>
	</BODY>
</HTML>
  ###########################
<!doctype html>
<HTML>
	<head>

	</head>
	<BODY>

	</ul>
	<br><br><br>
	
	<form name="kirjautuminen" action="http://127.0.0.1:8000/TehtKymppiTulos" method="get"; >
		
	Kirjoita kayttajanimi ja salasana <br>
	<br>
	Kayttajanimi: <br>
	<input type="text" name="nimi" value="" required><br> <!--required pakottaa laittaamaan arvon tuohon kenttaan -->
	Salasana: <br>
	<input type="password" name ="salasana" value="" required><br>
	<br>	
	<button onclick="kirjaudu">Kirjaudu</button>
	
	</form>
	
	</BODY>
</HTML>
