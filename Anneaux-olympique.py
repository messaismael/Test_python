from tkinter import *
coul = ['red','black','blue','yellow','green']
base = Tk( )
can = Canvas(base, bg='white', height=200,width= 335)
can.pack( )
bou = Button(base, text ="Quitter", command =base.quit)
bou.pack(side = RIGHT)
i = 0
x1, y1 = 20, 30
while( i< 5):
    can.create_oval(x1, y1, x1 + 100, y1+100, width =2, outline =coul[i])
    if(x1==220):
        x1, y1 = -30, 80
    x1 = x1 + 100
    i = i + 1
base.mainloop()