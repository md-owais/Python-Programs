# Break & Continue Statement in Python
# i = 0

# while(True):
#    if i+1<5:
#        i = i + 1
#        continue
#    print(i+1, end=" ")
#    if(i==44):
#       break  #stop the loop
#   i = i + 1

"""
while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number quarter than 100")
        break
    else:
        print("Try again!\n")
        continue
"""

"""
# Python program to demonstrate
# break statement

# Python program to
# demonstrate break statement
s = 'owaisalam'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'a'
    # or 's'
    if letter == 'a' or letter == 's':
        break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
    print(s[i])

    # break the loop as soon it sees 'a'
    # or 's'
    if s[i] == 'a' or s[i] == 's':
        break
    i += 1

print("Out of while loop")

"""

"""
# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
"""

# Python program to demonstrate
# pass statement
s = "owaisalam"
# Empty loop
for i in s:
    # No error will be raised
    pass


# Empty function
def fun():
    pass


# No error will be raised
fun()

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)
