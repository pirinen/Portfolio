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
  #Tietokantaan vientiä Djangolla
  #Views.py tiedostot
  #nimet.html & Teht8.html tahan tiedostoon
  
class Henkilo(object):

    nimi = "?"
    sukunimi = "?"

    def __init__(self, nimi, sukunimi):

        self.nimi = nimi
        self.sukunimi = sukunimi
        
def Teht8(request):

    if request.method == 'POST':

        form = NimiForm(request.POST)
    else:
        form = NimiForm()

    return render(request, 'Teht8.html', {'form': form})
    
def Teht8Tulos(request):
        #Tietokantayhteys alkaa
    conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
    print ("Opened database successfully")
    cur = conn.cursor()    #Paa-olio
    cur.execute("SELECT ID, etunimi, sukunimi from Person")
    rows = cur.fetchall()
    henkilot = []   #Henkilot-lista
    for row in rows:

        h1 = Henkilo(row[1], row[2])    #lisaillaan riveja muuttujaan joka
        henkilot.append(h1)             #sijoitetaan listaan

    t = get_template('nimet.html')
    lm = t.render(Context({'henkilot' : henkilot}))
    return HttpResponse(lm)
