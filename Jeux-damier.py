from tkinter import *
from random import randrange
fen1= Tk( )
can1 = Canvas(fen1, height= 500, width=500, bg= 'white')
can1.pack(padx=10, pady=10 )
def piont( ):
    n = randrange(10)
    u = randrange(10)
    x1, y1 = 12.5+n*50, 12.5+u*50
    can1.create_oval( x1,y1, x1+25, y1+25, fill ='red')
def carre( ):
    global l1, h1
    can1.create_rectangle(l1, h1, l1 + 50, h1 + 50, fill='black')
def dams():
    global l1, h1
    i = 0
    while( i < 5):
        carre( )
        l1 +=100
        i = i+ 1
def dam( ):
    global l1, h1
    i = 0
    while( i <= 5):
        if( i == 5):
            h1 += 50
        carre( )
        l1 += 100
        i = i + 1
def damier( ):
    global l1, h1
    l1, h1 = 0, 0
    i = 1
    while( i < 11):
        dams( )
        l1 = 100
        if( i%2==0):
            l1 = 50
            h1 += 50
            dam()
        l1 = 0
        i += 1
bou1 = Button(fen1,text='piont', command = piont)
bou1.pack(side = RIGHT )
bou2 = Button(fen1, text='damier', command = damier)
bou2.pack(side = LEFT )
fen1.mainloop( )