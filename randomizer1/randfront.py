from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import randback
import random

#Ostateczna funkcja guzika-generatora feed dla listy1
def generate():
    list1.delete(0,END)
    if CheckVar1.get() == 1 and RadVar.get() == 1 :
        for row in randback.searchallbox(1):
            list1.insert(END, row)
    elif CheckVar1.get() == 1 and RadVar.get() == 2 :
        for row in randback.searchallbox(2):
            list1.insert(END, row)
    elif CheckVar1.get() == 1 and RadVar.get() == 3 :
        for row in randback.searchallbox(3):
            list1.insert(END, row)
    elif CheckVar1.get() == 0 and RadVar.get() == 1 :
        for row in randback.searchA(1,dt2.day,dt2.month,dt2.year,dt1.day,dt1.month,dt1.year):
            list1.insert(END, row)
    elif CheckVar1.get() == 0 and RadVar.get() == 2 :
        for row in randback.searchA(2,dt2.day,dt2.month,dt2.year,dt1.day,dt1.month,dt1.year):
            list1.insert(END, row)
    elif CheckVar1.get() == 0 and RadVar.get() == 3 :
        for row in randback.searchA(3,dt2.day,dt2.month,dt2.year,dt1.day,dt1.month,dt1.year):
            list1.insert(END, row)
    else:
        pass

def date1():
    global dt1
    dt1=cal.selection_get()
    list3.delete(0,END)
    list3.insert(END, dt1)
    top.destroy()

def date2():
    global dt2
    dt2=cal.selection_get()
    list4.delete(0,END)
    list4.insert(END, dt2)
    top.destroy()

def calsel1():
    global clse
    clse = 1
    calselect()

def calsel2():
    global clse
    clse = 2
    calselect()

def calselect():
    global top
    top = Toplevel(window)
    l1 = ttk.Label(top, text='Wybierz datę')
    l1.pack(padx=10, pady=10)

#Ustaw tak, żeby na kalendarzu zawsze wyskakiwała pierwsza i/lub ostatnia data z bazy danych.
    global cal
    cal = Calendar(top, font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(padx=10, pady=10)
    if clse == 1:
        z1 = ttk.Button(top, text='ok', command=date1)
    elif clse == 2:
        z1 = ttk.Button(top, text='ok', command=date2)
    z1.pack(padx=10, pady=10)

def roll():
    randcommand(vi=1)

def randcommand(vi):
    list2.delete(0,END)
    if RadVar.get() == 1 and vi == 1 :
        list2.insert(END, sorted(random.sample(list(range(1,81)),k=20)))
    elif RadVar.get() == 2 and vi == 1 :
        list2.insert(END, sorted(random.sample(list(range(1,50)),k=6)))
    elif RadVar.get() == 3 and vi == 1 :
        list2.insert(END, sorted(random.sample(list(range(1,43)),k=5)))
    elif RadVar.get() == 4 and vi == 1 :
        lst1 = []
        lst1.append(sorted(random.sample(list(range(1,36)),k=5)))
        lst1.append(random.sample(list(range(1,5)),k=1))
        list2.insert(END, lst1)
    else:
        pass


window=Tk()

l1=Label(window,text="Wybierz rodzaj gry:")
l1.grid(row=0,column=2)
l2=Label(window,text="Zaznacz pomiary:")
l2.grid(row=2,column=0)
l4=Label(window,text="Całość pomiarów:")
l4.grid(row=3,column=0)
l6=Label(window,text="Generuj statystyki dla wybranego okresu:")
l6.grid(row=4,column=0,columnspan=2)
l7=Label(window,text="Najczęstsza i najrzadsza liczba:")
l7.grid(row=5,column=0)
l8=Label(window,text="Najczęściej padające liczby:")
l8.grid(row=6,column=0)
l9=Label(window,text="Ilość liczb:")
l9.grid(row=6,column=2)
l10=Label(window,text="Średnie wyników losowań:")
l10.grid(row=7,column=0)
l11=Label(window,text="Generuj wykres:")
l11.grid(row=7,column=2)
l12=Label(window,text="Generuj raporty")
l12.grid(row=8,column=0)
l13=Label(window,text="Zapisz raport:")
l13.grid(row=8,column=2)
l14=Label(window,text="Zagraj w wybraną grę:")
l14.grid(row=15,column=0)

list3=Listbox(window, height=1, width=10)
list3.grid(row=2,column=2)

list4=Listbox(window, height=1, width=10)
list4.grid(row=3,column=2)

d1 = ttk.Button(window, text='Wybierz datę', command=calsel1)
d1.grid(row=2,column=3)

d2 = ttk.Button(window, text='Wybierz datę', command=calsel2)
d2.grid(row=3,column=3)

list1=Listbox(window, height=8,width=80)
list1.grid(row=9,column=0,rowspan=6,columnspan=4)

list2=Listbox(window, height=1, width=60)
list2.grid(row=16,column=0,columnspan=3)
sb1=Scrollbar(window)
sb1.grid(row=9, column=4, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="Generuj", width=12, command=generate)
b1.grid(row=8,column=1)
b1=Button(window,text="Zapisz", width=12)
b1.grid(row=8,column=3)
b1=Button(window,text="Losuj", width=12, command=roll)
b1.grid(row=15,column=3)
b1=Button(window,text="Zamknij", width=12, command=window.destroy)
b1.grid(row=16,column=3)

RadVar= IntVar()
r1 = Radiobutton(window, text="MultiMulti", variable=RadVar, value=1)
r1.grid(row=1,column=0)
r2 = Radiobutton(window, text="Lotto", variable=RadVar, value=2)
r2.grid(row=1,column=1)
r3 = Radiobutton(window, text="Mini Lotek", variable=RadVar, value=3)
r3.grid(row=1,column=2)
r4 = Radiobutton(window, text="Ekstra Pensja", variable=RadVar, value=4)
r4.grid(row=1,column=3)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
c1 = Checkbutton(window, variable = CheckVar1, onvalue = 1, offvalue = 0)
c1.grid(row=3,column=1)
c2 = Checkbutton(window, variable = CheckVar2, onvalue = 1, offvalue = 0)
c2.grid(row=5,column=1)
c3 = Checkbutton(window, variable = CheckVar3, onvalue = 1, offvalue = 0)
c3.grid(row=6,column=1)
c4 = Checkbutton(window, variable = CheckVar4, onvalue = 1, offvalue = 0)
c4.grid(row=7,column=1)
c5 = Checkbutton(window, variable = CheckVar5, onvalue = 1, offvalue = 0)
c5.grid(row=7,column=3)


window.mainloop()
