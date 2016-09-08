# -*- coding: utf-8 -*-
    #Jukka Pirinen        8.9.2016
    #Tietokantaan vientiä ja tuontia
    # windows sovelluksessa
    
from tkinter import *
import psycopg2

    #--------------------------------------
def LisaaNimi():        #LISAA NIMI ALKAA
    ID = int(Entry.get(IDKentta))
    etunimi = str(Entry.get(etunimiKentta))
    sukunimi = str(Entry.get(sukunimiKentta))

    conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO Person (ID,etunimi,sukunimi) \
                VALUES (%s,%s,%s);",(ID,etunimi,sukunimi)); #Laitetaan tiedot tietokantaan
    conn.commit()
    
    listaBoksi.delete(0,END)    #Poistaa listan paivitysta varten
    cur.execute("SELECT ID, etunimi, sukunimi from Person") #---

    rows = cur.fetchall()
    
    for row in rows:
        listaBoksi.insert(row[0],row[1] + " " + row[2]) #---
    conn.close()
                        #LISAA NIMI LOPPUU
    #--------------------------------------
def PoistaNimi():       #POISTA NIMI ALKAA
    conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    poistettava = listaBoksi.curselection() #Valittuna oleva nimi
    print(poistettava)  #TestiPrinttaus
    cur.execute("DELETE from Person where ID=%s;", (poistettava))
    listaBoksi.delete(poistettava)  #Poistaa valitun listaboksista
    conn.commit()
    
    listaBoksi.delete(0,END)    #Poistaa listan paivitysta varten
    
    cur.execute("SELECT ID, etunimi, sukunimi from Person") #---

    rows = cur.fetchall()   #Ja tehdaan uusi lista
    for row in rows:
        listaBoksi.insert(row[0],row[1] + " " + row[2]) #---
    conn.close()
                       #POISTA NIMI LOPPUU
    #--------------------------------------

    
root=Tk()
root.title("Tietokannat")
root.geometry("450x350")    #Ikkunan koko
    
        #Luodaan framet
frame1=Frame(root, borderwidth=5)
frame1.pack()
frame2=Frame(root, borderwidth=5)
frame2.pack()
frame3=Frame(root, borderwidth=5)
frame3.pack()
frame4=Frame(root, borderwidth=5)
frame4.pack()
frame5=Frame(root, borderwidth=5)
frame5.pack()
        #Tekstit
teksti1=Label(frame1, text="ID             ")
teksti1.pack(side=LEFT)
teksti2=Label(frame2, text="Etunimi   ")
teksti2.pack(side=LEFT)
teksti3=Label(frame3, text="Sukunimi")
teksti3.pack(side=LEFT)
        #Kentat
IDKentta = Entry(frame1, width=14)
IDKentta.pack(side=RIGHT)
etunimiKentta = Entry(frame2, width=14)
etunimiKentta.pack(side=RIGHT)
sukunimiKentta = Entry(frame3, width=14)
sukunimiKentta.pack(side=RIGHT)
    
            #Listbox

listaBoksi = Listbox(frame5)    #ListBoxin luonti
conn = psycopg2.connect(database="test", user="postgres", password="jukka", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()    #Paa-olio
cur.execute("SELECT ID, etunimi, sukunimi from Person")
rows = cur.fetchall()
for row in rows:
    listaBoksi.insert(row[0],row[1] + " " + row[2])
listaBoksi.pack()
    
        #Button
btnLuoTaulu=Button(frame4, text="Lisää", command=LisaaNimi, height = 1, width = 16)
btnLuoTaulu.pack(side=RIGHT)
btnLuoTaulu=Button(frame4, text="Poista", command=PoistaNimi, height = 1, width = 16)
btnLuoTaulu.pack(side=RIGHT)

    
#conn.close()    #Suljetaan yhteys
root.mainloop()
