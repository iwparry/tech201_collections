# Lists

# Lists == Arrays



# here's our first list

shopping_list = ['milk', 'eggs', 'bread', 'fruit', 'cheese']
# print(type(shopping_list))
# print(shopping_list)
# # Lists are '0' indexed
# print(shopping_list[0]) # will print out 'milk'
# print(shopping_list[3]) # fruit
# print(shopping_list[-1]) # cheese

# We can change a value in the list

# shopping_list[0] = 'sugar' # overwrites the element at index 0 in shopping_list
# print(shopping_list) # returns ['sugar', 'eggs', 'bread', 'fruit', 'cheese']

# adding a new item

shopping_list.append('vegetables') # adds the element 'vegetables' to the end of our list
# print(shopping_list)
# print(len(shopping_list))

# remove an item

shopping_list.remove('bread') # removes the element 'bread' from our list
# print(shopping_list)
# print(len(shopping_list))

# remove last item from list, without specification

# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

# Mixed datatype lists

# mixt_list = [1, 2, 3.5, "one", "two", "three"]
# print(mixt_list)
#
# List slicing
#
# print(mixt_list[1:3]) # [2, 3.5]
# print(mixt_list[-2::]) # should reverses the order of the slice ['three', 'two']
# print(mixt_list[::2]) # misses every 2nd index - returns [1, 3.5, 'two']

# Tuples

# Exactly the same as list except they are immutable (cannot be changed)
# Tuples are useful for elements that you do not wish to be overwritten

# essentials = ("bread", "eggs", "milk")
# print(essentials)
# print(essentials.count("bread"))
# essentials.append("chocolate") # cannot add to tuples
# print(type(essentials)) # <class 'tuple'>
