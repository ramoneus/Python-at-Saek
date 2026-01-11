x = float(input('Δώσε ποσό χρημάτων πήρανε : '))
g = int(input('ήμερες γιωρίκα : '))
k = int(input('ήμερες κωστίκα : '))              
days = x  / (g+k)
money =  g* days
kmoney = k* days                                                   
print('ο Γιωρίκας θα πάρει',money,'€')
print('Ο Κωστίκας θα πάρει',kmoney,'€')                                                   
