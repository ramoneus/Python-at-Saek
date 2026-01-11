total = 0
with open('klaseis.txt', 'r') as f:
    for line in f:
        y = line.split()
        print(y)
        total += int(y[2])
print(total)
