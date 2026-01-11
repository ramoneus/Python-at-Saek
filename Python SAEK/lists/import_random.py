import random

num_students = 2
num_grades = 2

ON = [] 
grades = [] 

count_between_40_60 = 0
count_below_50 = 0
max_total = -1
max_name = ""

for i in range(num_students):
    name = input('Δώσε όνομα μαθητή: ')
    ON.append(name)
    student_grades = [random.randint(1, 100) for _ in range(num_grades)]
    grades.append(student_grades)

print("\nΒαθμοί μαθητών:")
for i in range(num_students):
    for j in range(num_grades):
        print(f"{grades[i][j]:7d}", end='')
    print()

for i in range(num_students):
    total = sum(grades[i])
    mo = total / num_grades
    for j in range(num_grades):
        if 40 < grades[i][j] < 60:
            count_between_40_60 += 1
        elif grades[i][j] < 50:
            count_below_50 += 1

    print(f"{ON[i]} -> Σύνολο: {total}, Μέσος όρος: {mo:.2f}")

    if total > max_total:
        max_total = total
        max_name = ON[i]

print(f"\nΑριθμός βαθμών μεταξύ 40 και 60: {count_between_40_60}")
print(f"Αριθμός βαθμών κάτω από 50: {count_below_50}")
print(f"Μέγιστο συνολικό βαθμό έχει ο {max_name} με {max_total}")
