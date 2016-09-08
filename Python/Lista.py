# -*- coding: utf-8 -*-
	#Jukka Pirinen      8.9.2016
	#Listat
	
lista = []
while True:
    print("Haluatko")
    print("(1)Lisata listaan")
    print("(2)Poistaa listalta vai")
    loop = input("(3)Lopettaa?:")
    if loop != "3":
        if loop == "1":
            lista.append(input("Mita lisataan:"))
        elif loop == "2":
            print("Listalla on",len(lista),"alkiota")
            try:
                lista.pop(int(input("Monesko niista poistetaan: "))-1)  #-1 nolla indeksin takia
            except IndexError:      #jos annettu indeksi on listan ulkopuolella
                print ("Virheellinen valinta")
        else:
            print("Virheellinen valinta")

    else:
        print("Listalla oli tuotteet:")
        for kaikki in lista:
            print(kaikki)
        break
