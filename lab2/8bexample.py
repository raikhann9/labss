#example1
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

#example2
i = 5
while i < 11:
    i += 1
    if i == 7:
        continue
    print(i)

#example3
i = 11
while i < 20:
    print(i)
    i += 1
else:
    print("i is no longer less than 20")

