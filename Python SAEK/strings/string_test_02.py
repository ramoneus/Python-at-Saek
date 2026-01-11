def anazitisi(key, CODE):
    for i in range(len(CODE)):
        if key == CODE[i]:
            return i
    return -1

TIMH = []
CODE = []
TEMA = []
ESODA = []

code = input('Δώσε κωδικό προιόντος του πρώτου προιόντος: ')
while code != 'ΤΕΛΟΣ':
    timh = float(input('Δώσε τιμή: '))
    tema = int(input('Δώσε τεμάχια: '))
    CODE.append(code)
    TIMH.append(timh)
    TEMA.append(tema)
    code = input('Δώσε κωδικό του επόμενου προιόντος: ')

for i in range(len(CODE)):
    esoda = TIMH[i] * TEMA[i]
    ESODA.append(esoda)

for i in range(len(CODE)):
    print(CODE[i], TIMH[i], TEMA[i], ESODA[i])

key = input('Δώσε κωδικό για αναζήτηση: ')
th = anazitisi(key, CODE)
if th == -1:
    print('Ο κωδικός δεν υπάρχει')
else:
    print(ESODA[th])
