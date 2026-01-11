def count_uppercase_words(words):
    count = 0
    for word in words:
        if word[0].isupper():
            count += 1
    return count

words = []
for i in range(5):
    word = input(f'Εισάγετε την {i+1}η λέξη: ')
    words.append(word)

uppercase_count = count_uppercase_words(words)
print(f"Από τις λέξεις που εισάγατε, {uppercase_count} έχουν το πρώτο γράμμα κεφαλαίο.")
