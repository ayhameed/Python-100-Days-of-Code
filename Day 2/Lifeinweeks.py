# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
con_age = int(age)
max_days = 365 * 90
max_weeks = 52 * 90 
max_month = 12 * 90

rem_days = max_days - (con_age * 365)
rem_weeks = max_weeks - (con_age * 52)
rem_months = max_month - (con_age * 12)

print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")