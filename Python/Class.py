# -*- coding: utf-8 -*-
    #Jukka Pirinen      8.9.2016
    #Class juttuja

class Henkilo():

    def __init__(self, etunimi="?", sukunimi="?", puhnro="0"): #muodostin henkilolle
        self.__etunimi = etunimi  #privateksi
        self.__sukunimi = sukunimi
        self.__puhnro = puhnro

    def setEtunimi(self, enimi):
        enimi = input("Anna henkilon etunimi: ")
        self.__etunimi = enimi#input("Anna henkilon etunimi: ")
    def setSukunimi(self, snimi):
        snimi = input("Anna henkilon sukunimi: ")
        self.__sukunimi = snimi
    def setPuhnro(self, nro):
        nro = input("Anna henkilon puhelinnumero: ")
        self.__puhnro = nro

    def getEtunimi(self):
        return self.__etunimi
    def getSukunimi(self):
        return self.__sukunimi
    def getPuhnro(self):
        return self.__puhnro

class Tyontekija(Henkilo):  #Periytyy henkilosta

    def __init__(self,palkka = 0,tyontekijaID = 0): #muodostin tyontekijalle
        super(Tyontekija,self).__init__(etunimi = "?", sukunimi = "?", puhnro = "0")    #kutsutaan henkilo luokan muodostinta
        self.__palkka = palkka
        self.__tyontekijaID = tyontekijaID

    def setPalkka(self, liksa):
        liksa = int(input("Anna henkilon palkka: "))
        self.__palkka = liksa
    def setTyontekijanID(self, ID):
        ID = int(input("Anna henkilon ID: "))
        self.__tyontekijaID = ID

    def getPalkka(self):
        return self.__palkka
    def getTyontekijaID(self):
        return self.__tyontekijaID


class Main():
    ihminen = Henkilo()
    print("Henkilo:")
    ihminen.setEtunimi("")
    ihminen.setSukunimi("")
    ihminen.setPuhnro("")
    print("Henkilo: Etunimi =",ihminen.getEtunimi(),", Sukunimi =", ihminen.getSukunimi(),", PuhNro =", ihminen.getPuhnro())
    duunari = Tyontekija()
    print("Tyontekija:")
    duunari.setEtunimi("")
    duunari.setSukunimi("")
    duunari.setPuhnro(0)
    duunari.setPalkka(0)
    duunari.setTyontekijanID(0)
    print("Tyontekija:", duunari.getEtunimi(), duunari.getSukunimi(),", PuhNro =", duunari.getPuhnro())
    print("Palkka =", duunari.getPalkka(),", ID nro =", duunari.getTyontekijaID())
    print()
