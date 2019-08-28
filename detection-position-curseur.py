from tkinter import *

def pointeur(event):
    chaine.configure( text="Clic détecté en X =" + str(event.x) +\
                           ", Y =" + str(event.y))
def cercle(event):
    x1,y1 = event.x-2, event.y-2
    can.create_oval(x1, y1, x1+4, y1+4, fill= 'red')
    chaine.configure(text="Clic détecté en X =" + str(event.x) + \
                          ", Y =" + str(event.y))
fen = Tk ( )
can = Canvas( fen, width = 200, height = 150, bg = "light yellow")
can.bind( "<Button-1>", cercle)
can.pack( )
chaine = Label(fen)
chaine.pack( )

fen.mainloop( )