#example1
x = 4       
x = "Sally" 
print(x)

#example2
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#example3
x = 5
y = "John"
print(type(x))
print(type(y))

#example4
x = "John"
print(x)
x = 'John'
print(x)

#example5
a = 4
A = "Sally"
print(a)
print(A)

#example6
name = "John"
n_name = "Elta"
_n_name = "Elsa"
nName = "Max"
NAME = "Kay"
name1 = "Jay"


print(name)
print(n_name)
print(_n_name)
print(nName)
print(NAME)
print(name1)

#example7
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

#example8
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

#example9
x = "Python "
y = "is "
z = "awesomeE"
print(x + y + z)

#example10
x = 5
y = "Jay"
print(x, y)

#example11
x = "good"

def text():
  x = "awesome"
  print("Python is " + x)

text()

print("Python is " + x)

#example12
x = "rare"
def myfunc():
  global x
  x = "perfect"

myfunc()

print("Name is " + x)