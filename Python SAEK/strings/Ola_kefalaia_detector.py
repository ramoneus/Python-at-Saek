def check_all_uppercase(word):
    if word.isupper():
        print("Όλα κεφαλαία")
    else:
        print("Όχι όλα κεφαλαία")


word = input("Εισάγετε μία λέξη: ")
check_all_uppercase(word)
