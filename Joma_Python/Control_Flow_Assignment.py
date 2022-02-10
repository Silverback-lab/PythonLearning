# Problem 1: Fizzbuzz

# Write a Python function which iterates the integers from 0 to n. 
# For multiples of three, print "Fizz"  instead of the number, 
# and for the multiples of five, print "buzz". 
# For numbers which are multiples  of both three and five, print "fizzbuzz". 

def fizzbuzz(n):
    number = 0
    print("fizzbuzz")
    while number in range(n):
        number += 1
        if number % 15 == 0:
            print("fizzbuzz")
        elif number % 5 == 0:
            print("buzz")
        elif number % 3 == 0:
            print("fizz")
        else:
            print(number)
    return

fizzbuzz(15)


print("===========================")
print("NEXT CODE")
print("===========================")


# Problem 2: Multiply without usuing *

# Write a Python function which multiplies two values (a and b) without using the multiplication  symbol *.
#  Use addition and a while loop to write your function.

def multiply(a, b):
    c = 0
    i = 0
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
    elif a < 0:
        print('-', end = ""),
        a = abs(a)
    while i in range(a):
        i += 1
        c = c + b
    return print(c)
 
multiply(3, 5)
multiply(-4, 5)
multiply(-4, 2)

print("===========================")
print("NEXT CODE")
print("===========================")

# Problem 3: Output the first n prime numbers 

# Write a Python function that outputs the first n prime numbers: 

def is_prime(n):
    a, b = 2, 0
    if n > 1:
        while a < n:
            if n % a == 0:
                b += 1
            a += 1
        if b == 0:
            return True
        else:
            return False
    return
 
def prime_numbers(n):
    a, b = 0, 0
    while a < n:
        if is_prime(b):
            print(b)
            a += 1
        b += 1
    return
 
prime_numbers(5)
prime_numbers(7)