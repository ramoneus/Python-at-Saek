# This program will create a text file named 'onomata.txt' and write 30 names with ages.

def write_names_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(30):
            # Get user input for name and age
            name = input(f"Enter name #{i+1}: ")
            age = input(f"Enter age for {name}: ")
            # Write the name and age to the file
            file.write(f"{name}_{age}\n")

# Call the function and pass the desired file name
write_names_to_file('onomata.txt')
