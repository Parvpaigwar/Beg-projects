import random
import string
def generate_password(min_Length,number=True,special_charcter=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    charcters = letters
    if number:
        charcters += digits
    if special_charcter:
        charcters += special


    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password)<min_Length :
        new_password = random.choice(charcters)
        password += new_password

        if new_password in digits:
            has_number = True
        elif new_password in special:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_charcter:
            meets_criteria = meets_criteria and has_special 
    return password

print("welcome to password generator!")
min_len = int(input("Enter minimum length for your password : "))
number_ask = input("Do You want to add number in you password(Y/N) : ").lower() == "y"
special_ask  = input("Do want to add special character in your password(Y/N): ").lower() == "y"

password = generate_password(10,number_ask,special_ask)
print("Your password : ",password)