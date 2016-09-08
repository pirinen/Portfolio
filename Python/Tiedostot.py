# -*- coding: utf-8 -*-
    #Jukka Pirinen      8.9.2016
    #Tiedostoon tallennus

import pickle

class Henkilo():    #Henkilo-luokka alkaa

    def __init__(self, etunimi="?", sukunimi="?"):
        self.__etunimi = etunimi
        self.__sukunimi = sukunimi

    def setEtunimi(self, enimi):
        enimi = input("Anna etunimi: ")
        self.__etunimi = enimi

    def setSukunimi(self, snimi):
        snimi = input("Anna sukunimi: ")
        self.__sukunimi = snimi

    def getEtunimi(self):
        return self.__etunimi

    def getSukunimi(self):
        return self.__sukunimi

    def __str__(self):  #Tulostus
        return "Nimi: " + self.__etunimi + " " + self.__sukunimi


class Main():   #PaaOhjelma alkaa
    lista = []
    while True:
        print("(1) Anna nimi")
        print("(2) Tulosta nimet")
        print("(3) Talleta tiedostoon (nimet.dat)")
        print("(4) Lopeta")
        valinta = input("Mita haluat tehda?:")

        if (valinta) == "1":    #Lisataan
            print("1")
            heppu = Henkilo()
            heppu.setEtunimi("")
            heppu.setSukunimi("")
            #lista.append((heppu.getEtunimi(), heppu.getSukunimi()))    #Talla tallennuksella voi myos lukea tiedostosta
            lista.append(heppu)

        elif (valinta) == "2":  #Tulostetaan
            print()
            for kaikki in lista:
                print(kaikki)
            print()

        elif (valinta) == "3":  #Tallennetaan
            with open("nimet.dat", "wb") as tiedosto:
                pickle.dump(lista, tiedosto, pickle.HIGHEST_PROTOCOL)
            tiedosto.close()    #Tarpeen?
            print()
            print("Tallennettu")
            '''with open("nimet.dat", "rb") as tiedosto:
                luettu = pickle.load(tiedosto)  # Testailin miten lukee, ei tuolla nykyisella append(obj) jutulla osaa
            tiedosto.close()                    # objekteja lukea takaisin tiedostosta
            print(luettu)'''                    # mutta eihan tassa tehtavassa tarvinnutkaan kuin tallentaa
            print()

        elif (valinta) == "4":  #Lopetetaan
            print("Lopetetaan")
            break           #Loopin loppu
        else:
            print("Vaara valinta")
