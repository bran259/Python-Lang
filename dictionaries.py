# Dictionaries can also be used to store many types of data that would describe the dictionary object itself.
# A mapping object maps an immutable value to an arbitrary value. Where there are many types of sequences in Python, there is only one type of mapping: the dict, or dictionary.

# Dictionary Methods
# Getting Data

def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size, "Unknown size")

# print("Tall size:", pour_coffee("tall"))
# print("Grande size:", pour_coffee("grande"))
# print("Venti size:", pour_coffee("venti"))
# print("Unknown size:", pour_coffee("small"))


# Setting Data
# The simplest way is to just use bracket notation - [] - and the assignment operator,

my_dict = {
    "key_one": "value one",
    "key_two": "value two",
}

# update multiple fields:
my_dict.update({"key_one": "new value one", "key_two": "new value two"})

# add multiple fields:
my_dict.update({"key_three": "value three", "key_four": "value four"})

# add and update fields simultaneously:
my_dict.update({"key_three": "new value three", "key_four": "new value four", "key_five": "value five"})

# print(my_dict)
# prints {'key_one': 'new value one', 'key_two': 'new value two', 'key_three': 'new value three', 'key_four': 'new value four', 'key_five': 'value five'}

# you can also pass in tuples and arrays as arguments or use assignment operation:

my_dict = {
    "key_one": "value one"
}

# passing in an array of arrays
my_dict.update([["key_one", "new value one"], ["key_two", "value two"]])

# passing in an array of tuples
my_dict.update([("key_two", "new value two"), ("key_three", "value three")])

# passing in a tuple of arrays
my_dict.update((["key_three", "new value three"], ["key_four", "value four"]))

# passing in a tuple of tuples
my_dict.update((("key_four", "new value four"), ("key_five", "value five")))

# using assignment operation
my_dict.update(key_five="new value five", key_six="value six")

# print(my_dict)
# prints {'key_one': 'new value one', 'key_two': 'new value two', 'key_three': 'new value three', 'key_four': 'new value four', 'key_five': 'new value five', 'key_six': 'value six'}


# Iterating Over Dictionaries
# dict.items(), which returns an object that can be treated as a list of tuples of key/value pairs.

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

[item for item in my_dict.items()]
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
[key for key, value in my_dict.items()]
# ['a', 'b', 'c', 'd']
[value for key, value in my_dict.items()]
# [1, 2, 3, 4]
# print(my_dict)

# example
student_details = {
    "firstname": "brian",
    "lastname": "kimno",
    "address": {
        "city": "Nairobi",
        "zip-code": "12345"
    },
    "friends": ["brian", "daniel", "tobijah", "jebet"]
}

# print first Name
print(student_details["firstname"])

# print city
print(student_details["address"]["city"])

# print tobijah from friends
print(student_details["friends"][2])

