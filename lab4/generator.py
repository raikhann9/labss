#exercise1
import random
def myfunc(n):
    for i in range(n):
        yield i**2
n=int(input())
for j in myfunc(n):
    print(j)

#exercise2
import random
def myfunc(n):
    for i in range(n):
        if(i%2==0):
            yield i 
n=int(input())
newline=[]
for j in myfunc(n):
    newline.append(str(j))
print(','.join(newline))

#exercise3
def myfunc(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i 
n=int(input())
for j in myfunc(n):
    print(j)

#exercise4
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2
a=int(input())
b=int(input())
for j in squares(a, b):
    print(j)

#exercise5
def myfunc(n):
    while n >= 0:
        yield n
        n -= 1
n=int(input())
for i in myfunc(n):
    print(i)