# Collections Task - Waiter Program

# Writing a program that helps a waiter with their menu

starters = ['mini pizza', 'chicken strips', 'halloumi fries', 'salt and pepper chips']
mains = ['9 inch pizza', 'bangers & mash', 'chicken curry', 'fish & chips']
desserts = ['strawberry sundae', 'chocolate fudge cake', 'syrup sponge', 'raspberry cheesecake']
drinks = ['lemonade', 'apple juice', 'orange juice', 'bottle of beer']

order = [] # customer order
print("Welcome!") # Greeting
print("Here's our menu:") # Printing the menus for the user
print(starters)
print(mains)
print(desserts)
print(drinks)
# Prompt the user to input their choices
starter = input("What would you like as your starter? ")
print(starter)
order.append(starter) # each choice will be added to the empty list we've named 'order'
main = input(("And for your main course? "))
print(main)
order.append((main))
dessert = input("And what would you like for dessert? ")
print(dessert)
order.append(dessert)
drink = input(("And lastly, what would you like to drink? "))
print(drink)
order.append(drink)
# Now have order read back to user
print("Just to double check, is this your order?")
print(order)
