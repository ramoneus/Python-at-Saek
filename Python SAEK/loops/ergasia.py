hotel_names = []
hotel_reviews = []

while True:
    hotel_name = input('Δώσε όνομα ξενοδοχείου ή "ΤΕΛΟΣ" για τερματισμό: ')
    if hotel_name.upper() == 'ΤΕΛΟΣ':
        break

    reviews = []
    for i in range(10):
        while True:
            try:
                review = int(input(f'Δώσε βαθμολογία {i+1}ου πελάτη (1 έως 5): '))
                if 1 <= review <= 5:
                    reviews.append(review)
                    break
                else:
                    print('Λανθασμένη βαθμολογία. Πρέπει να είναι 1 έως 5.')
            except ValueError:
                print("Πρέπει να δώσεις αριθμό.")

    hotel_names.append(hotel_name)
    hotel_reviews.append(sum(reviews))

# Εμφάνιση συνολικών αξιολογήσεων
for i in range(len(hotel_names)):
    print(f'Το ξενοδοχείο "{hotel_names[i]}" έχει συνολική βαθμολογία {hotel_reviews[i]}.')

# Ξενοδοχείο με τη μεγαλύτερη βαθμολογία
max_reviews = max(hotel_reviews)
best_hotel = hotel_names[hotel_reviews.index(max_reviews)]
print(f'Το καλύτερο ξενοδοχείο είναι: {best_hotel} με συνολική βαθμολογία {max_reviews}.')

# Υπολογισμός ποσοστού ξενοδοχείων με συνολική βαθμολογία < 40
low_reviews_count = sum(review < 40 for review in hotel_reviews)
percentage_low_reviews = (low_reviews_count / len(hotel_names)) * 100 if hotel_names else 0
print(f'Ποσοστό ξενοδοχείων με συνολική βαθμολογία < 40: {percentage_low_reviews:.2f}%')
