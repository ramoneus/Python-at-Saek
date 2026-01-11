import random

machines_output = [[random.randint(1, 100) for _ in range(7)] for _ in range(20)]

print("Αποδόσεις μηχανών:")
for i, machine in enumerate(machines_output):
    print(f"Μηχανή {i+1}: {machine}")

for day in range(7):
    max_output = max(machines_output[machine][day] for machine in range(20))
    lucky_machines = [machine + 1 for machine in range(20) if machines_output[machine][day] == max_output]
    print(f"Ημέρα {day + 1}: Τυχερή(ές) μηχανή(ές) {lucky_machines} με απόδοση {max_output}")
