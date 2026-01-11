n = int(input('Πόσα παπούτσια θα αγοράσεις; '))
s = int(input('Πόσο κοστίζει κάθε παπούτσι; '))

if n > 18:
    poso = s * (n - 3)  
elif 10 <= n <= 18:
    poso = s * (n - 2)  
elif 5 <= n < 10:
    poso = s * (n - 1)  
else:
    poso = s * n 

print(f'Το ποσό είναι: {poso} €')
