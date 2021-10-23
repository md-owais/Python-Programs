# For Loops in Python
"""
list1 = [["Harry",1], ["Larry", 2], ["Carry", 3], ["Marie", 10]]
dict1 = dict(list1)

for item in dict1:
    print(item)
for item, lollypop in dict1.items():
    print(item, "and lolly is",lollypop)

"""
'''
items = [int, float, "Harry",5,3,66,54,45,30,25]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
'''



dict1= {"Best Python Course": "CodeWithHarry",
        "Best C Languge Course": "CodeWithHarry",
        "Harry Sir":"Tom Cruise Of Programming"
        }

for x,y in dict1.items():
    print(x, y)
    


