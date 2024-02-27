#Write a python program to convert snake case string to camel case string.
import re
txt=input()
def replacing_cases(txt):
    return re.sub("_([a-z])", lambda x: x.group(1).upper(), txt)
    
print(replacing_cases(txt))