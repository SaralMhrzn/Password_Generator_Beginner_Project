import string
import random

# Define character sets
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
numbers = list(string.digits)
symbols = list(string.punctuation)

# checking value of number given by user is digit or not
def get_number_input(prompt):
    while True:
        number = input(prompt)   # .isdigit() use garna string ma huna parxa 
        if number.isdigit():
            return int(number)   #number ko value int ma change gareko
        else:
            print("Please enter a valid number.")

# Get user inputs for the number of each type of character
number_for_password = get_number_input("How many numbers would you like in your password?\n=")
number_for_lower_alphabet = get_number_input("How many lower alphabets would you like in your password?\n=")
number_for_upper_alphabet = get_number_input("How many upper alphabets would you like in your password?\n=")
number_for_symbols = get_number_input("How many symbols would you like in your password?\n=")

# Initialize password list
password = []

# Add random numbers to the password list
for i in range(number_for_password):
    password.append(random.choice(numbers))

# Add random lowercase letters to the password list
for i in range(number_for_lower_alphabet):
    password.append(random.choice(lower_alphabet))

# Add random uppercase letters to the password list
for i in range(number_for_upper_alphabet):
    password.append(random.choice(upper_alphabet))

# Add random symbols to the password list
for i in range(number_for_symbols):
    password.append(random.choice(symbols))

# Shuffle the password list to ensure randomness
random.shuffle(password)

# Convert the list to a string
password = ''.join(password)

# Print the final password
print("Your generated password is:")
print(password)