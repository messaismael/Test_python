def comptecar( ca, ch):
    a = ca
    b =  ch
    i = 0
    u = len( b )
    t = 0
    while( i < u ):
        z =b[ i ]
        if( z == a ):
            t = t + 1
        else:
            print( )
        i = i + 1
    print('il y a ',      t,    '<',a,'>',    'dans votre chaine')
print('entrer le caractère à compter :')
ac = input( )
print('entrer la chaine à décompter :')
hc = input( )
comptecar(ac, hc )