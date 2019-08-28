from tkinter import *
base = Tk( )
can = Canvas(base, width=500, height=250, bg ='white')
can.pack( )
def drawoval1():
    x1, y1 = 20, 30
    can.create_oval(x1, y1, x1+100, y1+100, width=2, outline='red')
def drawoval2():
    x1, y1 = 120, 30
    can.create_oval(x1, y1, x1+100, y1+100, width=2, outline='green')
def drawoval3():
    x1, y1 = 220, 30
    can.create_oval(x1, y1, x1+100, y1+100, width=2, outline='black')
def drawoval4():
    x1, y1 = 70, 80
    can.create_oval(x1, y1, x1+100, y1+100, width=2, outline='yellow')
def drawoval5():
    x1, y1 = 170, 80
    can.create_oval(x1, y1, x1+100, y1+100, width=2, outline='blue')
bou1 = Button(base, text='1', command=drawoval1)
bou1.pack(side= LEFT )
bou2 = Button(base, text='2', command=drawoval2)
bou2.pack(side= LEFT )
bou3 = Button(base, text='3', command=drawoval3)
bou3.pack(side= LEFT )
bou4 = Button(base, text='4', command=drawoval4)
bou4.pack(side= LEFT )
bou5 = Button(base, text='5', command=drawoval5)
bou5.pack(side= LEFT )
bou6 = Button(base, text='Quitter', command=base.quit)
bou6.pack(side=RIGHT)
base.mainloop( )