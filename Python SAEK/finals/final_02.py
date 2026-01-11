f = open('onomata.txt', 'w')
on = input('Δώσε όνομα : ')
age = int(input('Δώσε ηλικία : '))
f.write(on+'\n')
f.write(str(age)+'\n')
on = input('Δώσε όνομα : ')
age = int(input('Δώσε ηλικία : '))
f.write(on+'\n')
f.write(str(age)+'\n')
f.close()
ON=[]
A=[]
pl = 1
f = open('onomata.txt', 'r')
for x in f:
    if pl % 2 == 1:
        ON.append(x[0:len(x)-1])
    else:
        A.append(int(x))
    pl += 1
print(ON)
print(A)




f.close()
