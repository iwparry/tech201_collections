# Dictionaries

# Dictionaries use key/value pairs

# key = reference to a particular object
# value = data storage mechanism you want to use

# Create a dictionary

# student_1 = {
#     "name": "Susan",
#     "stream": "DevOps",
#     "completed_lessons" : 4,
#     "completed_lessons_name": ["variables", "data_type", "set_up"]
# }
# # # Access data within a dictionary
# # print(student_1["stream"]) # DevOps
# # # How to access specific items in a dictionary
# # print(student_1["completed_lessons_name"][0]) # variables
# # # Changing a value in our dictionary
# # student_1["completed_lessons"] = 3
# # print(student_1["completed_lessons"])
# # # Removing items from a dictionary
# # student_1["completed_lessons_name"].remove("data_type")
# # print(student_1["completed_lessons_name"])
#
# # Dictionary methods
#
# print(student_1.keys()) # returns all the keys
#
# print(student_1.get("name")) # will get the value associated with the specified key
#
# print(student_1.values()) # returns all the values
#
# print(student_1.items()) # returns all the key-value pairs as a list of tuples with each tuple being a key-value pair

# Dictionary task

my_dictionary = {
    'first_name': 'Iwan',
    'last_name' : 'Parry',
    'age' : 25,
    'height_cm' : 173.7,
    'hobbies' : ['football', 'movies', 'gaming']
}
print(my_dictionary)
print(my_dictionary['first_name'] + " " + my_dictionary['last_name']) # full name
print(my_dictionary['hobbies'][0]) # favorite sport
print(my_dictionary.get('age')) # will return my age, 25
print(my_dictionary.items()) # returns a list of tuples, where each tuple is a key-value pair from my_dictionary