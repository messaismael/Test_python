#Calcule de la période d'une pendule
from math import sqrt, pi
print('entrer la longueur de la pendule  l :')
l =  float( input( ))
print( 'entrer la valeur de la peusanteur au lieu experimentale g :')
g = float( input( ))
t = 2*pi*sqrt(l/g)
print( 'la période de cette pendule est :', t)