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
    guess = input("Guess a letter: ").lower()
askUser()

#Check if guess is in chosen_word

# lenght of choosen word
def len_chosen_word1():
    global len_chosen_word
    len_chosen_word = len(chosen_word)
    
def guessWord():
    len_chosen_word1()
    guesses = 0
    alpha_count = 0
    global blanks
    blanks = []
    blank = blanks
    if guesses  < len_chosen_word:
        for alpha in chosen_word:
            alpha = alpha
            alpha_count+=1
            if guess in alpha:
                blank.append(guess) 
            else:
                blank.append('_')
            guesses+=1
    print(blank)
guessWord()

#search for occurence of blanks and replace

while '_' in blanks:
    askUser()
    guessWord()