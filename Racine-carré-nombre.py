from math import*
i = 0
while( i < 5):
    print('entrer un nombre :')
    nb = float(input())
    if( nb < 0 ):
        print('il ya erreur sur le nombre entrer')
    else:
        print('la racine carré de', nb, '=', sqrt(nb))
    i = i+ 1
