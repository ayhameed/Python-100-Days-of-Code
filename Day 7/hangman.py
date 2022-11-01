import random

#Create a list holding the words
word_list = ["ardvak","donkey", "baboon", "elephant", "Tiger"]

#randomly chose a word from word_list and assign it to a variable called chosen_word
def randomWord():
    for word in word_list:
        global chosen_word 
        chosen_word = random.choice(word_list)
    print(f"random word :" +chosen_word)
randomWord()

#ask the user to guess a letter and assign that to a variable called guess. convert to lower case
def askUser():
    global guess 
    guess = input("Guess a letter: ")
    guess = guess.lower()
askUser()

#Check if guess is in chosen_word

# lenght of choosen word
def len_chosen_word():
    global len_chosen_word
    len_chosen_word = len(chosen_word)
    
def guessWord():
    len_chosen_word()
    guesses = 0
    global blanks
    blanks = []
    if guesses  < len_chosen_word:
        for alpha in chosen_word:
            alpha = alpha
            if guess in alpha:
                blanks.append(guess)
            else:
                blanks.append('_')
            guesses+=1
guessWord()

print(blanks)