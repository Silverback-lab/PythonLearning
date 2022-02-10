# Functions = A function is a sequence of instructions that performm a specific task, Packaged as a unit. 
#reusable, flexable, Modular

# print is the funtion in the following command
print("This is a print Function")

print("-------------------------------")
print("-------------------------------")

def hello(name):
    greet = "Hi! " + name
    print(greet)

hello("Mike")


# def = define

# hello = Name

# (name) = input

# def hello(name):
#    greet = "Hi! " + name
#    print(greet)                     = Function definition 

#    greet = "Hi! " + name
#    print(greet)                     = Instructions

# hello("Mike")  = Calling the function and "Mike" is the input

# it prints Hi! Mike

print("-------------------------------")
print("-------------------------------")

'''
def tip_amount(tip_percentage, total):
    print("The total is: " + str(total))
    print("The tip percentage is: " + str
    (tip_percentage * 100) + "%")
    print("The tip amount will be: " + str(total * 
    tip_percentage))

tip_amount(0.20, 100)

print("-------------------------------")
print("-------------------------------")
#can reuse functions through out code by defining new parameters 

tip_amount(0.07, 23.45)
'''
print("-------------------------------")
print("-------------------------------")
# a cleaner way to write this is in pratical use is:

def tip_amount(tip_percentage, total):
    return total * tip_percentage

def buy_food(num_of_apples, num_of_pears, num_of_nuts):
    total_price = num_of_apples * 2.00 + num_of_pears * 3.00 + num_of_nuts * 0.05
    print("Welcome to Mike's Store")
    print("Today you bought: ")
    print(str(num_of_pears) + " pears")
    print(str(num_of_apples) + " apples")
    print(str(num_of_nuts) + " nuts")
    print("Your total is: $" + str(total_price))
    tips = tip_amount(0.15, total_price)
    print("Please tip me $" + str(tips))

buy_food(2, 3, 100)






