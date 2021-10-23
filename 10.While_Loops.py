# While Loops in Python

# Syntax
'''
while expression:
    statement(s)
'''

"""
# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Owais!")
"""

"""
# checks if list still
# contains any element
a = [1, 2, 3, 4]

while a:
    print(a.pop())
"""


"""
# Python program to illustrate
# Single statement while block
count = 0
while (count < 5): count += 1;print("Hello Owais")

"""

"""
# Prints all letters except 'a' and 's'
i = 0
a = 'OwaisAlam'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1
"""

"""
# Break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'owaisalam'

while i < len(a):
    if a[i] == 'a' or a[i] == 's':
        i += 1
        break

    print('Current Letter :', a[i])
    i += 1
"""

"""
# Example: Python while loop with pass statement
# An empty loop
a = 'owaisalam'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)
"""

"""
# Python program to demonstrate
# while-else loop

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
"""



# Example: Python while loop with user input
a = int(input('Enter a number (-1 to quit): '))

while a != -1:
    a = int(input('Enter a number (-1 to quit): '))








