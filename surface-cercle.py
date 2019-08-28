from math import pi
def surfcercle(r):
    return pi*r**2
print( 'entrer le rayon de votre cercle :')
i = float( input( ))
print(surfcercle(i))