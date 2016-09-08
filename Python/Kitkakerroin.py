#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-
	#Jukka Pirinen    8.9.2016
	#Kitkakerroinlaskuri

nopeus = 20
while True:
    kitkak = input("Anna kitkakerroin (0.1-0.8): ")
    kitkak = float(kitkak)
    if kitkak >= 0.1 and kitkak <= 0.8:
        for i in range(0,11):
            nopeus = nopeus + 10
            jmatka = (nopeus/3.6)**2/(2*kitkak*9.81)
            print("Jarrutusmatka nopeudesta", nopeus, "on", round(jmatka,2),"m")
    else:
        print("Kitkakerroin ei ole sallittu")
