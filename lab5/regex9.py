#Write a Python program to insert spaces between words starting with capital letters.
import re
txt=input()
x = re.findall("[A-Z][a-z]*", txt)
print(" ".join((x)))