import random

def generate_random_art():
    # Define the shapes
    shapes = ['Triangle', 'Square', 'Circle', 'Star']
    
    # Randomly select a shape
    shape = random.choice(shapes)
    
    # Generate the ASCII art
    if shape == 'Triangle':
        print("  /\  ")
        print(" /  \ ")
        print("/____\\")
    elif shape == 'Square':
        print(" ____ ")
        print("|    |")
        print("|____|")
    elif shape == 'Circle':
        print("  __  ")
        print("/    \\")
        print("\\____/")
    elif shape == 'Star':
        print("  *  ")
        print(" * * ")
        print("* * *")
        print(" * * ")
        print("  *  ")
    
    print(f"You got a {shape}!")

# Run the function
generate_random_art()
