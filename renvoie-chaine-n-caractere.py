# 7.2 Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca
def lignecar( n, ca ):
    i = 0
    while( i < n):
        print( ca )
        i = i + 1
print( 'entrer le nombre de ca :')
a = int( input( ) )
print( 'entrer ca :')
c = input( )
lignecar(a, c)