import os
from random import random
os.system('clear')


num = random()
num *= 100
num = int(round((num), 0))
num1 = str(num)

if (num > 50):
    print ("Your number is greater than 50, Your number was: " + (num1))

elif (num == 50):
    print ("Your number was 50!")


else:
    print ("Your number is smaller then 50, your number was: " + (num1))    