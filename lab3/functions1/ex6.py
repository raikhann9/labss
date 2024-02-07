#Reverse a string: we are here -> here are we
def reverse_str(str):
    word = str.split()
    i = len(word)-1
    while i >= 0:
        print(word[i], end=' ')
        i -= 1

str = input()
reverse_str(str)
