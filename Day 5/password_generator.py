#Password Generator Project

from itertools import count
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random.shuffle(letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(numbers)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(symbols)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#get the lenght of the letters and reverse it
letter_list = []
for i in range(nr_letters):
    letter_list.append(letters[i])
    letter_list.reverse()

#get the lenght of the symbols and reverse it
symbol_list = []
for j in range(nr_symbols):
    symbol_list.append(symbols[j])
    symbol_list.reverse()
    
#get the lenght of the symbols and reverse it
number_list = []
for k in range(nr_numbers):
    number_list.append(numbers[k])
    number_list.reverse()

#convert the lists to string
letter_pass = ''.join(str(e) for e in letter_list)
symbol_pass = ''.join(str(f) for f in symbol_list)
number_pass = ''.join(str(g) for g in number_list)
password = letter_pass + symbol_pass + number_pass

#randomizes the final concat string using random.sample
password_finall = ''.join(random.sample(password, len(password)))

#test
print(f"Generated password is : {password_finall} ")