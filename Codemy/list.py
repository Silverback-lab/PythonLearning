import os
os.system('clear')


# Lists

my_name = "Chris"
first_name = ["Mike", "John", "Bob", my_name]

print (first_name)
print (first_name[1])
print (first_name[3])


num = [1, 2, 3, 4, 5]
first_name.append(num)

print (first_name)
print (first_name[4][2])

del first_name[4]
print (first_name)
print(len(first_name))
print (first_name[len(first_name) - 1])