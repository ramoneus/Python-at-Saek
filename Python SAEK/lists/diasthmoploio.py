import random

vehicles = 15
missions_per_year = 12

ΠΟΣ = [[random.randint(100, 300) for _ in range(missions_per_year)] for _ in range(vehicles)]

for i in range(vehicles):
    sum_posothta = sum(ΠΟΣ[i])
    print(f"Διαστημικό όχημα {i+1}: {sum_posothta} κιλά πετρωμάτων")
