import random
from random import randrange
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_name = len(names)
random_payer_num = randrange(length_name)
payer = names[random_payer_num]
print(f"{payer} is going to buy the meal today!")