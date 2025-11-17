# while => executes a statement a number of times

# count = 0

# while count <= 10:
#     print(count)
#     count +=1

# for => iterating over the sequence
# fruits = ["Banana", "Apple", "Grapes", "Lemon", "Oranges", "kiwi"]

# for fruit in fruits:
#     print(fruit)
#     if fruit == "kiwi":
#         # print(fruit)
#         break


numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers_squared = list()
# for num in numbers:
#     # print(num * 2)
#     numbers_squared.append(num ** 2)

# print(numbers_squared)    

new_num_sq = [ num ** 2 for num in numbers ]
print(new_num_sq)