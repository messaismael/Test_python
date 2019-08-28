from tkinter import *
def avance1( gd, hd):
    global x1, y1
    x1, y1 = x1 + gd, y1 + hd
    can1.coords(oval1, x1,y1, x1+30,y1+30)
def avance2( gd, hd):
    global x2, y2
    x2, y2 = x2 + gd, y2 + hd
    can1.coords(oval2, x2,y2, x2+50,y2+50)
def depl_gauche1( ):
    avance1(-10, 0)

def depl_gauche2( ):
    avance2(-10, 0)

def depl_droite1( ):
    avance1(10, 0)

def depl_droite2( ):
    avance2(10, 0)

def depl_haut1():
    avance1(0, -10)

def depl_haut2():
    avance2(0, -10)

def depl_bas1( ):
    avance1(0, 10)

def depl_bas2():
    avance2(0, 10)

x1, y1 = 200, 150
x2, y2 = 100, 150
fen1 =Tk( )
fen1.title("Force gravitationnelle entre deux masses")
can1 = Canvas(fen1, bg ='dark grey', height=300,width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width =1, fill='red')
oval2 = can1.create_oval(x2, y2, x2+50, y2+50, width =1, fill='blue')
can1.pack(side =TOP)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
Button(fen1, text ='->', command=depl_droite1).pack(side=RIGHT )
Button(fen1, text ='<-', command=depl_gauche1).pack(side=RIGHT )
Button(fen1, text ='<-', command=depl_gauche2).pack( side=LEFT)

Button(fen1, text ='->', command=depl_droite2).pack(side=LEFT )
Button(fen1, text ='^', command=depl_haut1).pack(side=RIGHT )
Button(fen1, text ='^', command=depl_haut2).pack(side=LEFT )
Button(fen1, text ='v', command=depl_bas1).pack(side=RIGHT )
Button(fen1, text ='v', command=depl_bas2).pack(side=LEFT )

fen1.mainloop( )