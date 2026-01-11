highest_price = 0
highest_price_artist = ""
oldest_year = 3000
oldest_year_artist = ""
countA = 0
countB = 0
countC = 0
total = 0

while True:
    artist = input('Δώσε όνομα καλλιτέχνη (Α, Β, Γ) ή "." για τερματισμό: ')
    if artist == '.':
        break

    try:
        year = int(input('Εισάγετε έτος δημιουργίας του πίνακα: '))
        price = float(input('Εισάγετε τιμή πώλησης του πίνακα: '))
    except ValueError:
        print("Πρέπει να δώσεις έγκυρο αριθμό. Προσπάθησε ξανά.")
        continue

    if artist == 'Α':
        countA += 1
    elif artist == 'Β':
        countB += 1
    elif artist == 'Γ':
        countC += 1
    else:
        print("Άγνωστος καλλιτέχνης, αγνοείται.")
        continue

    total += price

    if price > highest_price:
        highest_price = price
        highest_price_artist = artist

    if year < oldest_year:
        oldest_year = year
        oldest_year_artist = artist

print(f"Η υψηλότερη τιμή στην οποία πωλήθηκε ένας πίνακας: {highest_price:.2f}€ και ο καλλιτέχνης είναι ο {highest_price_artist}")
print(f"Ο καλλιτέχνης με τον παλαιότερο πίνακα είναι ο {oldest_year_artist} και η ηλικία του πίνακα είναι {2026 - oldest_year} έτη")
print(f"Ο αριθμός των έργων του καλλιτέχνη Α: {countA}")
print(f"Ο αριθμός των έργων του καλλιτέχνη Β: {countB}")
print(f"Ο αριθμός των έργων του καλλιτέχνη Γ: {countC}")
