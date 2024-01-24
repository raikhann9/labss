#example1
a = '''Python is good,
Python is awesome,
Python is interesting.'''
print(a)

#example2
a = "Hello123"
print(a)

#example3
a = "Hi, World!"
print(a.upper())

#example4
a = "Hi, World!"
print(a.lower())

#example5
a = " Hello, World!      "
print(a.strip())

#example6
a = "Hi, World!"
print(a.replace("W", "D"))

#example7
a = "Hi, dear, World!"
b = a.split(",")
print(b)

#example8
a = "Hi"
b = "World"
d="!"
c = a + " " + b + d
print(c)

#example9
q = 3
i = 15
p = 50.95
myorder = "I want to pay {2} dollars for {0} pizzas of restaurant {1}."
print(myorder.format(q, i, p)) 

#example10
txt = "We need to read about \"Vikings\" from the north."
print(txt) 

#example11
b = "Hello, World!"
print(b[2:6])