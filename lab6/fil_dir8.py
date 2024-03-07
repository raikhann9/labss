#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
path_=r"D:\PP2\lab6\f1.txt"
def delete_f(path_):
    if os.path.exists(path_) and os.access(path_, os.W_OK):
        os.remove(path_)
        print("Successfully deleted!")
    else:
        print("Not deleted.")

delete_f(path_)