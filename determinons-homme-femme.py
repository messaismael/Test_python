print('entrer votre nom :')
nm =input( )
print('entrer votre sexe (M ou F) :')
sx =  input( )
m = "M"
f = 'F'
a = 0
while( a < 5):
    if( sx == m):
        print('Cher monsieur')
    elif(sx == f):
        print('Cher mademoiselle')
    else:
        print('entrer à nouveau  votre sexe (M ou F) :')
        sx = input()
    a = a + 1


