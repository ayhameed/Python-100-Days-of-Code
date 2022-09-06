import random
from random import randrange

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input(" What do you choose ? \n Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Display User Choice based on input
if choice == 0:
    print(f"Your choice is Rock \n {rock}")
elif choice == 1:
    print(f"Your choice is Paper \n {paper}")
elif choice == 2:
    print(f"Your choice is Scissors \n {scissors}")
else:
    print("Invalid Selection, restart game and select values within 0 and 1")
    
# geneate random numbers between 0 and 3 for computer's choice
comp_choice = randrange(3)
#choose random options based on number from random generator 
if comp_choice == 0:
    print(f"Computer's Choice is Rock \n {rock}")
elif comp_choice == 1:
    print(f"Computer's Choice is Paper \n {paper}")
elif comp_choice == 2:
    print(f"Computer's Choice is Scissors \n {scissors}")

#select a winner accorinding to the game's rule on https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

if choice == comp_choice:
    print("It is a draw!")
elif choice == 0 and comp_choice == 2:
    print("You win!")
elif choice == 2 and comp_choice == 1:
    print("You win!")
elif choice == 1 and comp_choice == 0:
    print("You win!")
else:
    print("You Loose!")