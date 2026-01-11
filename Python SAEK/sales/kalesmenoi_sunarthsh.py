
def f1(k):
    if k<=300:      y=8
    elif k<=800:    y=12
    elif k<=1500:   y=15
    else: y=20
    return y
    
    

k = int(input('Καλεσμένοι : '))
while k <=0 or k>2000 :
    k=int(input('Καλεσμένοι : '))
y = f1(k)
total = y * 50
print('Θα πληρώσετε',total,'€')
