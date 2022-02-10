# Control Flow  

# We use control structures to alter control flow 

def website_welcome(name, age):
  if age >= 18:
    print("Welcome " + name + "!")
    print(" You ar very old: " + str(age))

  else:
    print("You are not welcome, you are too young!")
    years_left = 18 - age
    print("Wait another " +  str(years_left) + " years")

'''---------------------------------------------------'''
'''---------------------------------------------------'''


def can_watch_movie(age, with_parents):
  if age >= 17:
    return True
  else:
    if with_parents:
      return True
    else:
      return False

'''
elif age < 17 and with_parents:
return True
else:
return False
'''

website_welcome("Mike", 16)


'''
greetings = "Welcome " + name + "!"
print(greetings)
year_born = 2020 - age
print("You were born in " + str(year_born))
'''


'''---------------------------------------------------'''
'''---------------------------------------------------'''

def eat_apples(num_of_apples, on_diet):
  apples_remaining = num_of_apples
  while apples_remaining > 0 and not on_diet:
    apples_remaining -= 1
    print("Thank you!")

  print("Done")
  print(apples_remaining)

  return
