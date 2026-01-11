hotel_names = []
hotel_scores = []

while True:
    hotel_name = input('Εισάγετε το όνομα του ξενοδοχείου: ')
    if hotel_name == 'ΤΕΛΟΣ':
        break
    scores = []
    for i in range(10):
        while True:
            score = int(input(f'Εισάγετε βαθμολογία από τον κριτή {i+1} (1-5): '))
            if 1 <= score <= 5:
                scores.append(score)
                break
            else:
                print('Μη έγκυρη βαθμολογία. Πρέπει να είναι από 1 έως 5.')
    hotel_names.append(hotel_name)
    hotel_scores.append(sum(scores))

for i in range(len(hotel_names)):
    print(f'Η συνολική βαθμολογία για το {hotel_names[i]} είναι: {hotel_scores[i]}')

max_score = max(hotel_scores)
best_hotel = hotel_names[hotel_scores.index(max_score)]
print(f'Το ξενοδοχείο με τη μεγαλύτερη συνολική βαθμολογία είναι το {best_hotel}')

low_score_count = sum(score < 40 for score in hotel_scores)
percentage_low_score = (low_score_count / len(hotel_names)) * 100
print(f'Το ποσοστό των ξενοδοχείων με συνολική βαθμολογία λιγότερη από 40 είναι: {percentage_low_score:.2f}%')
