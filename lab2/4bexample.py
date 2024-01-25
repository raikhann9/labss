#example1
thistuple = ("apple", "strawberry", "cherry", "apple", "cherry")
print(thistuple)

#example2
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#example3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#example4
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#example5
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)