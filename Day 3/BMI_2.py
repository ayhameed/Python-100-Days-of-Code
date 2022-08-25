# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
abs_height = float(height)
abs_weight = int(weight)

bmi = abs_weight / (abs_height * abs_height)
abs_bmi = round(bmi)

if bmi<18.5:
    print(f"Your BMI is {abs_bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {abs_bmi}, you have a normal weight.")
elif bmi > 25 and bmi <30:
    print(f"Your BMI is {abs_bmi}, you are slightly overweight.")
elif bmi > 40 and bmi > 35:
    print(f"Your BMI is {abs_bmi}, you are obese.")
else:
    print(f"Your BMI is {abs_bmi}, you are clinically obese.")