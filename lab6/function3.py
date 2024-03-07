#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
str=input()
str2=''.join(reversed(str))
if str==str2:
    print("It is a palindrome")
else:
    print("It is not palindrome")
