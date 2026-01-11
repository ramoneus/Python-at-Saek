def upologismos(timh, posothta):
    """
    Υπολογίζει το συνολικό κόστος ανάλογα με την ποσότητα:
    - >18 τεμάχια: έκπτωση 3 τεμαχίων
    - 10-18 τεμάχια: έκπτωση 2 τεμαχίων
    - 10 τεμάχια: έκπτωση 1 τεμαχίου
    - <=9 τεμάχια: καμία έκπτωση
    """
    if posothta > 18:
        total_timh = timh * (posothta - 3)
    elif posothta >= 10:
        total_timh = timh * (posothta - 2)
    elif posothta > 9:
        total_timh = timh * (posothta - 1)
    else:
        total_timh = timh * posothta
    return total_timh

# Main
timh = int(input('Δώσε τιμή παπουτσιών: '))
posothta = int(input('Δώσε πόσα παπούτσια αγοράστηκαν: '))

sunoliko_kostos = upologismos(timh, posothta)
print(f'Η ομάδα πρέπει να πληρώσει συνολικά: {sunoliko_kostos} €')
