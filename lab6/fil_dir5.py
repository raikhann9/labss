#Write a Python program to write a list to a file.
items = ['Mango', 'Orange', 'Apple', 'Lemon']
with open("f2.txt",'w') as f:
    for i in items:
        f.write(i + "\n")