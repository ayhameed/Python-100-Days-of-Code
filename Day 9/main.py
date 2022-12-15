#creating a dictionary with key and value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retriving from a dictionary
print(programming_dictionary["Bug"])

#writing to a dictionary 
programming_dictionary["Loop"] = "Repeat a set of instructions until a condition is met"
print(programming_dictionary)

#create an empty dictionary 
empty_dictionary = {}