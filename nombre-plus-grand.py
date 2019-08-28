def maximum( n1, n2, n3):
    max = 0
    if( n1 >= n2) & (n1 >= n3):
        max = n1
    elif( n2 >= n1) & ( n2 >= n3):
        max = n2
    else:
        max = n3
    print('le plus grand nombre des trois est :', max )
print('entrer le nombre n°1 :')
a = float( input( ))
print('entrer le nombre n° :')
b = float( input( ))
print('entrer le nombre n°3 :')
c = float( input( ))
maximum( a, b, c)