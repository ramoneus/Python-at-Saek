class Mathitis:
    def __init__(self, am,on,ap):
        self.am = am
        self.on = on
        self.ap = ap
    def emfanise(self):
        print (self.am, self.on, self.ap)
    def change_ap(self,x):
        self.ap += x

L=[]
for i in range(3):
    am = int(input('am = '))
    on = input('on = ')
    ap = int(input('ap = '))
    a = Mathitis(am,on,ap)
    L.append(a)
f = open('klaseis.txt','w')
for i in range(3):
    f.write(str(L[i].am)+' '+L[i].on+' '+str(L[i].ap)+'\n')
f.close()
sum = 0
for i in range(3):
    sum += L[i].ap
f = open('klaseis.txt','a')
f.write('total = '+str(sum)+'\n')
f.close()





