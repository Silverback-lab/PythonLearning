import os
from random import random
os.system('clear')

# Conditional statements
# If
# Else
# Elif
#
#I had some fun with this LOL
#
def get_random():
    num = random()
    num *= 100
    num = int(round((num), 0))
    return num
#num1 = str(num)

#F string structure
#print(f"number = {num}")
count = 0
while count < 20:
    num = get_random()
    if (num > 50):
        print (f"Your number is greater than 50, Your number was {num}")
        

    elif (num == 50):
        print (f"your number was 50!")

    else:
        print (f"Your number is smaller then 50, your number was {num}")

    count += 1


# Will this run on mac 