# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# calculate the lenght of student height 

len_student = 0
for std in student_heights:
    len_student +=1

#iterate each number on the list and sum
sum = int(0)
for height in student_heights:
    sum +=height

#divide the sum of numbers on list by the lenght of list
average_height = sum / len_student
print(round(average_height))