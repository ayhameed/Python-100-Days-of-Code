# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#get length of string
len_score = 0
for scores in student_scores:
    len_score+=1
# store the first item on the list for comparison
largest = student_scores[0]

#compare values
i = 0
for i in range((len_score-1)):
    i+=1 
    if student_scores[i] > largest:
        largest = student_scores[i]
    
print(f"The lenght  of the string is : {largest}")       
print(f"The largest number is : {largest}")


