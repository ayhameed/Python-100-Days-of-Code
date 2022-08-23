#Calculate the percentage to be given as tip
#Objective: learn arithmetic operations and control flow

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $")) 
number_of_people = int (input("How many people to split the bill? "))
percentage_tip = int(input("What percentage tip would you like to give? "))

tip = float(percentage_tip  / 100) * total_bill
bill_and_tip = float(total_bill + tip) 
bill_per_person = float(bill_and_tip/ number_of_people)
final_bill= "{:.1f}".format(bill_per_person) 
print("Each person should pay: $",final_bill)
