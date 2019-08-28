t =  [32, 5, 12, 8, 3, 75, 2, 15]
t1 =[]
t2 = []
i = 0
b = len(t)
while( i < b):
    if(t[i]%2==0):
        t1.append(t[i])
    else:
        t2.append(t[i])
    i = i + 1
print( t1, t2)