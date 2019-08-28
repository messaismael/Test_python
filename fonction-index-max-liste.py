def indexmaxliste(liste):
    u = liste
    a = len(u)
    i  = 0
    b = 0
    n = 0
    while( i < a):
        z = u[i]
        if( z >= b ):
            b = z
            n = i
        i = i + 1
    print(   n  )
i = 0
serie =[ ]
while( i < 5):
    print(' entrer un nombre ')
    a = float(input( ))
    serie.append(a)
    i =  i + 1
indexmaxliste(serie)








