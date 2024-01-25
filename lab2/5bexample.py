#example1
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#example2
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#example3
thisset = {"apple", "banana", "carrot"}
thisset.discard("banana")
print(thisset)

#example4
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#example5
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
