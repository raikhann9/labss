#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
str=input()
count1=0
count2=0
for i in str:
    if i.isupper():
        count1+=1
    elif i.islower():
        count2+=1

print(count1, "and", count2)