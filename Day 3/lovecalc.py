# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#concat both names and convert to
both_names = name1+" "+name2
both_names.lower()

#Check occurences in TRUE 
T = both_names.count('t')
R = both_names.count('r')
U = both_names.count('u')
E = both_names.count('e')
Total_true = int(T + R + U + E)

#Check occurences in LOVE
L = both_names.count('l')
O = both_names.count('o')
V = both_names.count('v')
E = both_names.count('e')
Total_love = int(L + O + V + E)

love_score = str(Total_true) + str(Total_love)

int_love_score = int(love_score)

if int_love_score < 10 and int_love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int_love_score >= 40 and int_love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")