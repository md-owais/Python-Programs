# String Slicing and Other Function

mystr = "owais is a good boy"
#print(len(mystr))
#print(mystr[0:19])
"""
print(mystr[78])
print(mystr[0:78])
print(mystr[0:5:2])
print(mystr[0:]) #This will print whole
print(mystr[:5]) #This will take zero also
print(mystr[:]) #This will take whole length
print(mystr[::]) #By default it will take 1
print(mystr[-1:0])
print(mystr[-4:-2])
print(mystr[::-1])  #This will reverse the string
print(mystr[::-2]) #this will skip one one letter
"""
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.endswith("bdoy"))
print(mystr.count("b"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))