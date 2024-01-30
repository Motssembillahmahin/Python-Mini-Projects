#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#easy way
password = ""
for char in range(1, nr_letters + 1) :
    primary_select = random.choice(letters)
    password += primary_select
for num in range(0, nr_numbers + 1) :
    primary_select2 = random.choice(numbers)
    password += primary_select2
for sym in range(0,nr_symbols + 1) :
    primary_select3 = random.choice(symbols)
    password += primary_select3
print(password)
password_list = []
for x in range(0, nr_letters) :
    password_list.append(random.choice(letters))
for x in range(0, nr_symbols) :
    password_list.append(random.choice(symbols))
for x in range(0, nr_numbers) :
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password_hard = ""
for y in password_list :
    password_hard += y
print(password_hard)