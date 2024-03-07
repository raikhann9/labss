#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def checking_tuple(elements):
    return all(elements)

print(checking_tuple((True, False, False)))
print(checking_tuple((True, True, True)))
print(checking_tuple((False, False, False)))