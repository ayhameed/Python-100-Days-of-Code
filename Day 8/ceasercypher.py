#holds all the alphabet used for encryption 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#imports the logo art from a different py file and prints it
from art import logo
print(logo)

#keep the program running until user says otherwise


decision = True
while decision:
    #Accept user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #keeps the shift number within range
    if shift > 26 :
        shift = shift % 26

    #A fucntion that encrypts text
    def encrypt(plain_text, shift_amount):
        #loop through each letter in the plain text and work out position in alphabet list
        encrypted_text = ""
        for letter in plain_text:
            current_position =  alphabet.index(letter)
            new_position = current_position + shift_amount
            new_letter = alphabet[new_position]
            encrypted_text += new_letter
        print(f"The encoded text is {encrypted_text}")
        
    #A function that decrpts texts
    def decrypt(encrypted_text, shift_amount):
        decrypted_text = ""
        for letter in encrypted_text:
            current_position =  alphabet.index(letter)
            original_position = current_position - shift_amount
            original_letter = alphabet[original_position]
            decrypted_text += original_letter
        print(f"The decoded text is {decrypted_text}")

    #If statements that calls either the encrypt() or decrypt() based on user input
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    else:
        decrypt(encrypted_text=text, shift_amount=shift)
        
    decision_a = input("Would you like to continue, please type 'yes' otherwise 'no': ")
    if decision_a == "no":
        decision = False
        print("Goodbye")