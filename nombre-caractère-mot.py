ch = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
i = 0
a = len(ch)
t1 = []
t2 = []
while( i < a):
    z = ch[i]
    if( len(z)<=6):
        t1.append( z)
    else:
        t2.append(z)
    i = i + 1
print(t1, t2)
