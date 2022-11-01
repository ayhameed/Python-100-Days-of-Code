import random

#Create a list holding the words
word_list = ["donkey", "baboon", "elephant", "Tiger"]

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
def guessWord():
    len_chosen_word = len(chosen_word)
    guesses = 0

    if guesses  < len_chosen_word:
        for alpha in chosen_word:
            alpha = alpha
            if guess in alpha:
                print("right")
            else:
                print("wrong")
            guesses+=1
guessWord()