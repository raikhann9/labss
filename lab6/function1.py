#Write a Python program with builtin function to multiply all the numbers in a list
import math
def multip_ly(list):
     return math.prod(list)
     
list1 = [1, 2, 5, 4, 8]
print("Product:", multip_ly(list1))