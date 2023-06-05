#Import logo from art.py and print it in the console. 
from art import logo
print (logo)

def add(n1, n2):
    """Adds two numbers together and returns the sum"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers and returns the difference"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers and returns the product"""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers and returns the quotient"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide    
}
continue_op = True
while continue_op != False:
    n1 = int(input("What's the first number?: "))
    n2 = int(input("What's the second number?: "))
    for operation in operations:
        print(operation)
    operation_symbol = input("Pick an operation from the line above: ")
    answer = (operations[operation_symbol]) (n1, n2)
    print (f"{n1} {operation_symbol} {n2} = {answer}")

    continue_op =  input("Would you like to perform another calculation? Y to continue / N to end ")
    continue_op.upper()
    if continue_op != 'Y':
        continue_op = False
        break