import os
os.system('clear')

fav_pizza = {
    "John": "Pepperoni",
    "Bob": "Cheese",
    "Mike": "Supreme"
}

print (fav_pizza)
print (fav_pizza["Bob"])

del fav_pizza["John"]
print (fav_pizza)

fav_pizza["John"] = "Ham"
print (fav_pizza)

fav_pizza.update({
"Tim": "Green Peppers"

})

print (fav_pizza)
print (fav_pizza["Tim"])