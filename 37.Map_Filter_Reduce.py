"""
Map
Syntax: map(function, iterable)
Example:
items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x **3), items))
print(a)
#Output: [1, 8, 27, 64, 125]

Filter
Syntax: filter(function, iterable)
Example:
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c) # prints out [2, 5, 3]
"""


# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# print((square))


# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# print((square))

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# # num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# ----------------------FILTER------------------
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
#-----------------------Reduce------------------
from functools import reduce

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)










































































