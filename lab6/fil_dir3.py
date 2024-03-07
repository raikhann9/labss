#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
path_=r"D:\PP2\lab6\f1.txt"
if os.path.exists(path_):
    print(os.path.basename(path_))
    print(os.path.dirname(path_))
else:
    print("No such path")