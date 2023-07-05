chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

chocolate_type = input('Which type of chocolate would you like?')

print("That will cost")
print(chocolates[chocolate_type])