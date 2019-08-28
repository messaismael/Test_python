from tkinter import *
from random import randrange
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1,y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1+10
def drawline2():
    global a1, b1, a2, b2
    can1.create_line(a1, b1, a2, b2, width=2)
    b2, b1 = b2+ 422500,b1-422500
def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]
x1, y1, x2, y2 = 0, 10, 500, 10
a1, b1, a2, b2 = 0, 325, 500, 325
coul = 'dark green'
fen1 = Tk()
can1 = Canvas(fen1,bg='dark grey',height=650,width=500)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4 = Button(fen1, text='viser', command=drawline2)
bou4.pack()
fen1.mainloop() # démarrage du réceptionnaire d’événements
fen1.destroy()