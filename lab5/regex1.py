#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
txt=input()
x = re.findall("ab*", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


