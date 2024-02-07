#Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def print_perm():
    str = input()
    variants = permutations(str)
    for i in variants:
        print(''.join(i))

print_perm()