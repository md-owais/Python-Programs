# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

def funargs(normal, *argsowais, **kwargs):  #kwargsowais also can write
    print(normal)
    for item in argsowais:
        print(item)
        print("\nNow I would like to introduce some of our Heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


# function_name_print("Owais", "Harry", "Rohan", "Hammad")

har = ["Owais", "Harry", "Rohan", "Hammad"]
normal = "I am a normal argument and the student are:"
kw = {"Owais":"Monitor", "Harry":"Fitness Instructor"}
funargs(normal, *har, **kw)