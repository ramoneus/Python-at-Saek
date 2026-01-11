import random

# Δημιουργία λίστας με τυχαία παραγωγή αυγών 10 ημερών
production = [random.randint(1, 1000) for _ in range(10)]

print("Παραγωγή ανά ημέρα:", production)

# Υπολογισμός μέσου όρου
average = sum(production) / len(production)
print(f"Μέση ημερήσια παραγωγή: {average:.2f}")

# Εύρεση ημερών με παραγωγή πάνω από τον μέσο όρο
print("Ημέρες με παραγωγή πάνω από τον μέσο όρο:")
for i, eggs in enumerate(production):
    if eggs > average:
        print(f"Ημέρα {i+1}: {eggs} αυγά")
