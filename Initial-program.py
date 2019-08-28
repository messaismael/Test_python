from tkinter import *
fen1 = Tk( )
txt1 = Label(fen1, text ='Premier champ :')
txt2 = Label(fen1, text =' Second :')
txt3 = Label(fen1, text ='troisième :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)

can1 = Canvas(fen1, width=250, height=200, bg='white')
photo = PhotoImage(file ='good.gif')
item = can1.create_image(80, 80, image =photo)

txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
entr1.grid(row =1, column =1)
entr2.grid(row =2, column =1)
entr3.grid(row =3, column =1)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)

fen1.mainloop( )