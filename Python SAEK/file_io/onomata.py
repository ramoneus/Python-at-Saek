with open('onomata.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        name = input(f'Εισάγετε το όνομα {i+1}: ')
        f.write(name + '\n')

names = []
with open('onomata.txt', 'r', encoding='utf-8') as f:
    for line in f:
        names.append(line.strip()) 

print("Ονόματα:", names)
