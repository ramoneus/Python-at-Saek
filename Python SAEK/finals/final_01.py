plA=plB=plC=sum=0
min = 2024
max = -1
on = input('Δώσε το πρώτο όνομα : ')
while on != '.':
    etos = int(input('Δώσε έτος : '))
    timi = float(input('Δώσε τιμή : '))
    if timi > max :
        max = timi
        maxName = on
    if etos < min :
        min = etos
        minName = on
    if on == 'A': plA += 1
    if on == 'B': plB += 1
    if on == 'C': plC += 1
    sum += timi
    on = input('Δώσε το επόμενο όνομα : ')

if max == -1:
    print ('Δεν διαβάστηκαν δεδομένα')
else:
    print(maxName,max, minName,min, plA, plB, plC, sum)
