#Calcule du périmètre et de la surface d'un triangle quelconque
from math import sqrt
e = input( "entrer le coté a :")
u = input( "entrer le coté b :")
i = input( "entrer le coté c :")
a = int(e)
b = int(u)
c = int(i)
p = a + b + c
print('le périmètre de ce triangle est :', p )
d = p/2
s =  sqrt(d*(d-a)*(d-b)*(d-c))
print( 'la surface de ce triangle est :', s)