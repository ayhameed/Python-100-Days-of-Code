
import random

test_seed = int(input("Create a Seed Number : "))

test_seed = random.randint(0, test_seed)
print(test_seed)

if test_seed == 1:
    print("Heads.")
else:
    print("Tails.")


#test
