# Set elements are unique. Duplicates are not supported.
# Set elements are unordered. This means that they cannot be accessed by index.
# Sets are mutable, but can only store immutable data.

my_list = [1, 2, 1, 3, 2]
set(my_list)
# {1, 2, 3}
# print(my_list)

my_string = "the big red cat ate the fat rat"
set(my_string)
# {'g', 'h', 'b', 'r', 'e', 'd', 'f', 'c', 't', 'a', 'i', ' '}
# print(my_string)

set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# True
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 & set_2
# 3
# print(set)

thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)