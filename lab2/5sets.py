#task1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#task2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#task3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#task4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#task5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)