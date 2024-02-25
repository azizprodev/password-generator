# password generator
import random
import string

def generate_password(min_length, numbers = True, special_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special_char = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special_char = True


        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_char:
            meets_criteria = meets_criteria and has_special_char

    return pwd


min_length = int(input("Enter minimum length: "))
has_number = input("Do you want have number (y/n)? ").lower() == "y"
has_special = input("Do you want special character (y/n)? ").lower() == "y"
password = generate_password(min_length, has_number, has_special)
print(password)