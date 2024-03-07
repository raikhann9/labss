#Write a Python program to write a list to a file.
n=input()
thislist=list(n)
with open("f2.txt",'w') as f:
    for i in thislist:
        f.write(str(i)+" ")