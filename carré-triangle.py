from turtle import *
def triangle(base ):
    i = 0
    while( i < 3):
        color('blue')
        forward( base)
        right( 120)
        i = i + 1
def carre( taille ):
    i = 0
    while( i < 4 ):
        color('red')
        forward( taille )
        right( 90 )
        i = i + 1
i =  0
a = 50
up( )
goto(-500, 0)
while( i < 5 ):
    down( )
    carre(a)
    up()
    forward(a+10)
    down( )
    triangle(a)
    up()
    forward(a+10)
    i = i + 1
    a = a + 20





