# BMI CALCULATOR
#Formular weight(kg) / height^2 (m)

height = float (input ("Please enter Height in (m)"))
weight = float (input ("Please enter weight in (KG)"))

bmi = weight / (height * height)
print ("Your BMI is : ",int(bmi))
