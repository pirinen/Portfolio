# -*- coding: utf-8 -*-
    #Jukka Pirinen      8.9.2016
    #Dictionary

class Tyontekija():

    tyontekijat = {"123" : ["Matti", "Meikalainen"],
                   "321" : ["Minna", "Meikalainen"],
                   "132" : ["Tiina", "Tomera"]}

class Main():
    duunari = Tyontekija()
    print("Dictionary sisaltaa seuraavat tyontekijat (yht", len(duunari.tyontekijat),"kpl)")
    for ID, [nimi,snimi] in duunari.tyontekijat.items():
        print("ID:{0}\nEtunimi: {1}\nSukunimi: {2}".format(ID, nimi,snimi))
