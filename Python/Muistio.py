# -*- coding: utf-8 -*-
    #Jukka Pirinen      8.9.2016
    #Muistion tekeminen

while True:
    print("(1) Lue muistikirjaa")
    print("(2) Lisaa merkinta")
    print("(3) Tyhjenna muistikirja")
    print("(4) Lopeta")
    print()
    valinta = input("Mita haluat tehda?:")

    if (valinta) == "1":
        muistio = open("muistio.txt", "r")  #Avataan muistio
        while True:
            sisalto = muistio.readline()
            if len(sisalto) == 0:
                break
            print(sisalto, end = "")
        muistio.close
    elif (valinta) == "2":
        muistio = open("muistio.txt", "a")  #Avataan muistio
        lisaa = input("Kirjoita uusi merkinta:")
        lisaa = lisaa + "\n"
        muistio.writelines(lisaa)
        muistio.close
    elif (valinta) == "3":
        muistio = open("muistio.txt", "w")  #Avataan
        muistio.close()                     #ja suljetaan muistio tyhjennyksen takia
        print("Muistikirja tyhjennetty")
    elif (valinta) == "4":
        print("Lopetetaan")
        break   #loopin loppu
    else:
        print("Tuntematon valinta")
