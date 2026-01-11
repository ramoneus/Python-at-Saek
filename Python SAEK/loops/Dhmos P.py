a = []
t = []

for i in range(1, 1501):
    name = input(f'Δώσε όνομα αθλητή #{i}: ')
    try:
        time = float(input('Δώσε χρόνο αθλητή σε δευτερόλεπτα: '))
    except ValueError:
        print("Πρέπει να δώσεις αριθμητικό χρόνο. Προσπάθησε ξανά.")
        continue

    a.append(name)
    t.append(time)

# Βρες τον ταχύτερο αθλητή
fastest_index = t.index(min(t))
print(f'Ο αθλητής που τερμάτισε πρώτος είναι ο {a[fastest_index]} με χρόνο {t[fastest_index]:.2f} δευτερόλεπτα.')
