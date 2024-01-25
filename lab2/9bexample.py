#example1
for x in "tomato":
    print(x) 

#example2
fruits = ["apple", "cherry", "banana", "grape", "orange"]
for x in fruits:
    print(x) 
    if x == "banana":
        break

#example3
for x in range(2, 19, 4):
    print(x)

#example4
for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")

#example5
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
