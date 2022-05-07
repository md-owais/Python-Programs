'''
#tutmain1.py
print("__name__ in tutmain1.py is set to"+__name__)
output:
__name__ in tutmain1.py is set to __main__
'''

'''
#tutmain2.py
import tutmain1

print("__name in tutmain2.py is set to"+__name__)

output:
__name__ in tutmain2.py is set to tutmain1

Syntax:
if__name__=="__main__":
    #Logic Statement
'''

# CODE
def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)

