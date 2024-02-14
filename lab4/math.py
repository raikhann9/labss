#exercise1
import math
degree=int(input("Input degree: "))
print("Output radian:", math.radians(degree))

#exercise2
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
area=((a+b)*h)/2
print("Expected Output:", area)

#exercise3
import math
n=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
area=(n*(l**2))/(4*math.tan(math.pi/n))
print("The area of the polygon is:", int(area))

#exercise4
l=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
print(float(l*h))


