# Lists and List Functions

grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]
"""
print(grocery)
print(grocery[0])
print(grocery[2])
#print(grocery[6]) #This will show error
"""
numbers = [2, 7, 9, 11, 3]
#print(numbers[2])
#numbers.sort()
#numbers.reverse()
#print(numbers[0:5])  #print(numbers[:5]) are same or print(numbers[:])
"""
print(numbers[1:])
print(numbers[1:4])  #slicing print lists
print(numbers[::1])
print(numbers[::2])
print(numbers[::-1])  #Don't take -2 or -3 always take -1
#print(numbers.sort())
"""
#numbers = []
#numbers.append(71)
#numbers.append(1)
#numbers.append(7)
#numbers.insert(3,23)
#numbers.remove(9)
#numbers.pop()
#print(numbers)

numbers[1] = 98
print(numbers)
#mutable = can change
#immutable = cannot change
#tp = (1,)
#print(tp)
a = 1
b = 8
a, b = b,a
#temp= a
#a = b
#b = temp
print(a, b)