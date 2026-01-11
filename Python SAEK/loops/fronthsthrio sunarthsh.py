def place(mo):
    if 9.5 <= mo < 13.5:
        return 'g4'
    elif 13.5 <= mo < 16.0:
        return 'g3'
    elif 16.0 <= mo < 18.5:
        return 'g2'
    elif 18.5 <= mo <= 20.0:
        return 'g1'
    else:
        return 'Μη έγκυρος μέσος όρος'

count_g2 = 0
count_1719 = 0

while count_g2 < 30:
    on_math = input('Δώσε όνομα μαθητή: ')
    try:
        mo = float(input('Δώσε τον μέσο όρο του μαθητή της Β λυκείου: '))
    except ValueError:
        print("Μη έγκυρος αριθμός, προσπάθησε ξανά.")
        continue

    if 17.0 <= mo <= 19.0:
        count_1719 += 1

    tmhma_mathiti = place(mo)
    print(f'Ο μαθητής {on_math} εισήχθη στο τμήμα {tmhma_mathiti}')

    if tmhma_mathiti == 'g2':
        count_g2 += 1

print(f'Ο αριθμός των μαθητών στο τμήμα g2 είναι: {count_g2}')

pos1719 = (count_1719 / 30) * 100
print(f'Το ποσοστό των μαθητών με μέσο όρο 17.0-19.0 είναι: {pos1719:.2f}%')
