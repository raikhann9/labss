#Write a Python program to convert a given camel case string to snake case.
import re
txt=input()
def replacing_cases(txt):
    return re.sub("([a-z])([A-Z])", lambda x: x.group(1)+"_"+x.group(2).lower(), txt)
    
print(replacing_cases(txt))
