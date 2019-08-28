def changecar( ch, ca1, ca2, debut = 0, fin = -1 ):
    if( fin == -1):
        fin = len(ch)
    nch = ''
    i = 0
    while( i < len(ch)):
        if( i >= debut )&( i <= fin )&( ca1 == ch[i] ):
           nch = nch + ca2
        else:
            nch = nch + ch[i]
        i = i + 1
    return nch
print('entrer une phrase : ')
phrase = input()
print(changecar(phrase, 's', '*', 3, 15))