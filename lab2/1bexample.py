#example1
x = 200
print(isinstance(x, int))

#example2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#example3
def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

#example4
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#example5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
