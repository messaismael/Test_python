from turtle import *
def etoile5( base ):
    a = 0
    while(a < 5):
        a = a + 1
        color('blue')
        forward(base)
        left(144)
def carre( taille ):
    i = 0
    while( i < 4 ):
        color('red')
        forward( taille )
        left( 90 )
        i = i + 1
def triangle(base ):
    i = 0
    while( i < 3):
        color('blue')
        forward( base)
        left( 120)
        i = i + 1
def etoile6(base):
    a = 0
    while a <3:
        color('blue')
        forward(base)
        left(120)
        a = a +  1
    up( )
    left(90)
    forward( base/2 )
    right( 90)
    down( )
    b = 0
    while (b < 3):
        color('blue')
        forward(base)
        right(120)
        b = b + 1
i =  0
a = 20
up( )
width( 2 )
goto(0, -100)
while( i < 9 ):
    down( )
    etoile5(a)
    up()
    forward(a + 10)
    down( )
    triangle(a)
    up()
    forward(a + 10)
    down()
    etoile6( a )
    up()
    forward( a )
    left(60)
    forward( 10)
    down()
    carre(a)
    up( )
    forward(a+ 10)
    i = i + 1
    a = a + 5
a = input( )
