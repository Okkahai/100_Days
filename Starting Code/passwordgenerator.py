import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

char_pool = []

for _ in range(nr_letters):
    char_pool.append(random.choice(letters))

for _ in range(nr_symbols):
    char_pool.append(random.choice(symbols))

for _ in range(nr_numbers):
    char_pool.append(random.choice(numbers))

total_char_num = len(char_pool)

password = ""

for _ in range(total_char_num):
    index = random.randint(0, len(char_pool) - 1)
    password += char_pool.pop(index)

print(f"Your password is: {password}")
