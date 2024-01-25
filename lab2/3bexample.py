#example1
list1 = ["apple", "strawberry", "cherry"]
list2 = [13, 5, 7, 6, 8]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#example2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example3
thislist = ["strawberry", "orange", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example4
thislist = ["strawberry", "orange", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#example5
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)