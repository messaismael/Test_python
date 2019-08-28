from turtle import *
def etoile( base ):
    a = 0
    while(a < 3):
        color('green')
        forward(base)
        left(120)
        a = a+1
    up()
    left(90)
    forward(base / 2)
    right(90)
    down()
    b = 0
    while (b < 3):
        color('green')
        forward(base)
        right(120)
        b = b + 1
etoile(50)