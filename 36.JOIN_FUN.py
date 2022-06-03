'''
# Syntax
# string.join(iterable)

Example:
#join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

output:
1, 2, 3, 4
'''

list = ["Jhon", "cena", "Randy", "ortan",
        "Sheamus", "Khali", "jinder mahal"]

# for item in list:
#     print(item, "and", end=" ")

# a = " and ".join(list)
a = " , ".join(list)
print(a, "Other WWE superstars")