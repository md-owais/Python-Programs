#Dictionary and it's Functions in Python
#Dictionary is nothing but key value pairs
#d1 = ()  #This is for blank tuple
'''
d1 = {}
#print(type(d1))
d2 = {"Owais":"Burger",
      "Rohan":"Fish", "skillf":"Rohit",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
#d2["Ankit"] = "Junk Food"
#d2[420] = "kebabs"
#del d2[420]
"""
print(d2)
print(d2["Owais"])
print(d2["Rohan"])
print(d2["Shubham"]["B"])

#print(d2)
print(d2.copy())
d3 = d2.copy()
del d3["Owais"]
"""
#print(d2.get("Owais"))
#print(d2.update({"Leena":"Toffee"}))
#print(d2.keys())
print(d2.items())

'''


'''
# Create a dictionary and take input  from the user and return the meaning of the
# word from the dictionary

D={'Ram': '12.2.2000',
   'Rahul': '11.23.1998',
   'Owais': '12.6.2000',
   'Pin': '854311'
   }
name =input("Enter the name :")
print(D[name])

"""
Dict={"Owais":"Alam"}
key=input{"Type key for Dict"}
print(Dict[key])
"""

"""
word=input("Enter your word")
Dict={"hoolignism":"voilent","purblind":"lacking in vission"}
print(dict[word]) """

'''


"""
# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# # a = funcret(1)
# a = funcret(0)
# print(a)

# def executor(func):
#     func("this")
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_owais():
    print("Owais is a good boy")

# who_is_owais = dec1(who_is_owais)
who_is_owais()
"""