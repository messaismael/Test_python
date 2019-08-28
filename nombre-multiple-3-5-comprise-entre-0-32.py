#programme qui additionne les nombresmultiples de 3 et de 5 compris entre 0 et 32
a = 0
b = 0
while (a < 100 ):
    if( a%3 == 0 )&( a%5 == 0 ):
        print( a, '+', end = ' '  )
        b = b + a
    a = a + 1
print( '=', b )

