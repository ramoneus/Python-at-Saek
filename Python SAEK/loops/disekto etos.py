# Εισαγωγή δεδομένων

try:
    month = int(input('Δώσε αριθμό μήνα (1-12): '))
    year = int(input('Δώσε έτος: '))
except ValueError:
    print("Πρέπει να δώσεις έγκυρους αριθμούς.")
    exit()

if month < 1 or month > 12:
    print("Μήνας πρέπει να είναι από 1 έως 12.")
    exit()

# Έλεγχος αν είναι δίσεκτο έτος
def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# Υπολογισμός ημερών
if month == 2:
    days = 29 if is_leap_year(year) else 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

print(f"Ο μήνας {month}/{year} έχει {days} ημέρες.")
