# Decorator: syntax that allows us to add functionality to an object without modifying its structure.

# def hello(name):
#     return "Hello " + name

# print(hello("Guido"))
# # Hello Guido

# greeting = hello
# print(greeting("Guido"))

# def salutation(func):
#     return func("Guido")

# print(salutation(greeting))

# def hello(name):
#     print("Hello from the hello() function.")

#     def greet():
#         print("Greetings from the greet() function.")

#     return greet

# def decorator(func):
#     def wrapper():
#         print("I am the output that lets you know the function is about to be called.")
#         func()
#         print("I am the output that lets you know the function has been called.")
#     return wrapper

# def get_called():
#     print("I am the function and I am being called.")

# @decorator
# def get_called():
#     print("I am the function and I am being called.")
# get_called()



# def sweep_floors(time):
#     if 1100 < time < 2100:
#         print("Sweeping the floors...")
#     else:
#         print("I'm off duty!")


# def wash_dishes(time):
#     if 1100 < time < 2100:
#         print("Washing the dishes...")
#     else:
#         print("I'm off duty!")

# def chop_vegetables(time):
#     if 1100 < time < 2100:
#         print("Chopping the vegetables...")
#     else:
#         print("I'm off duty!")

def check_vowel(letter):
    letter = letter.lower()
    return (letter == "a" or
            letter == "e" or
            letter == "i" or
            letter == "o" or
            letter == "u")
print(check_vowel("a"))
