#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
filename = "f1.txt"

print("It does exist:", os.access(filename, os.F_OK)) 
print("Readable:", os.access(filename, os.R_OK)) 
print("Writable:", os.access(filename, os.W_OK))
print("Executable:", os.access(filename, os.X_OK))