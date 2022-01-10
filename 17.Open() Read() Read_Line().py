# File IO Basics
"""
"r" -Open file for reading
"w" -Open file for writing
"x" - Creates file if not exists
"a" -Add more content to a file
"t" -text mode
"b" -binary mode
"+" -read and write
"""
f = open("owais.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
# content = f.read(34455)
# print("2", content)
f.close()