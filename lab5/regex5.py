#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt=input()
x = re.findall("a.*b$", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")