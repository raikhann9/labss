#Write a Python program to copy the contents of a file to another file
with open('f1.txt', 'w+') as f:
    f.write("I want to read a book")
    f.seek(0) 
    x = f.read()
with open('f2.txt', 'w') as y:
    y.write(x)