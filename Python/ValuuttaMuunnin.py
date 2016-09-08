# -*- coding: utf-8 -*-
    #Jukka Pirinen      8.9.2016
    #Valuuttamuunnin, windows sovellus

from tkinter import*
import tkinter.messagebox as mbox

def doNone():
    pass

def tulos():
    try:
        eurot2 = float(Entry.get(eurot))
        
        if kolikot.get() == 1:      #SEK
            muunnos = eurot2 * 7.21
        elif kolikot.get() == 2:    #GBP
            muunnos = eurot2 * 0.78
        elif kolikot.get() == 3:    #USD
            muunnos = eurot2 * 1.56
        Entry.delete(tulos, 0, END)
        Entry.insert(tulos, 0, round(muunnos,2))

    except ValueError:
        mbox.showinfo("Syote virheellinen          ")
        eurot.delete(0, END)


    #Main alkaa
root=Tk()
root.title("Kolikonmuunnin")
root.geometry("350x200")

kolikot = IntVar()
kolikot.set(1)

hilut = [("SEK", 1),("GBP", 2),("USD", 3)]
    #Framet
frame=Frame(root)
frame.pack()
frame2=Frame(root, borderwidth=5)
frame2.pack()
frame3=Frame(root, borderwidth=5)
frame3.pack()
frame4=Frame(root, borderwidth=5)
frame4.pack()
    #Btn
btnMuutos=Button(frame3, text="  Muuta  ", command=tulos)
btnMuutos.pack(side=RIGHT)
    #Labelit & tekstit
eurot=Label(frame, text="Euro      ")
eurot.pack(side=LEFT)
eurot=Entry(frame, width=20)
eurot.pack(side=RIGHT)

tulos=Label(frame4, text="Muunnos uudessa valuutassa  ")
tulos.pack(side=LEFT)
tulos=Entry(frame4, width=20)
tulos.pack(side=RIGHT)

for txt, val in hilut:  #RadioButtonit
    Radiobutton(frame2,
                text=txt,
                padx = 20,
                variable = kolikot,
                command = doNone,
                value = val).pack(anchor=W)

root.mainloop()
