T=[]
for i in range (5):
    t =float(input('Τιμή λαμπάδας: '))
    while t<=0:
        t=float(input('Λάθος. Τιμή λαμπάδας: '))
    T.append(t)

sum = 0
for i in range(len(T)):
    sum = sum + T[i]
mo = sum/len(T)
print('Ο μέσος όρος είναι',mo)

pl=0
for x in T:
    if x>10:
        pl += 1

print('Το πλήθος είναι: ',pl)