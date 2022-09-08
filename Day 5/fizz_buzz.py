#if num % 3 == 0 print Fizz
#if num % 5 == 0 print Buzz
#if num % 3 == 0 and num % 5 == 0 print Fizz_buzz

for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")