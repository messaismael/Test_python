from turtle import *
def etoile( base ):
    a = 0
    while( a < 5 ):
        a = a + 1
        color('blue')
        forward(base)
        right(144)
i = 0
a = 50
up( )
goto(-500, 50)
while( i < 5 ):
    down( )
    etoile( a )
    up( )
    forward( a + 20)
    i = i + 1
    a = a + 10
a = 80
i = 4
while( i > 0 ):
    down( )
    etoile( a )
    up( )
    forward( a + 20)
    i = i - 1
    a = a - 10
a = input( )



