#Checking if a given string is a palindrome or not
def palindrome_str(txt):
    rev=txt[::-1]
    if(txt==rev):
        return True
    else:
        return False

txt=input()
print(palindrome_str(txt))