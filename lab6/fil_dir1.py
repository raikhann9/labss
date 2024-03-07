#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path_ = r"D:\PP2"
all_i=os.listdir(path_)
for i in all_i:
    if os.path.isdir(path_):
        direcs=os.path.join(path_, i)
    if os.path.isfile(path_):
        filess=os.path.join(path_, i)

print("directories:", direcs)
print("files:", filess)
print("all items:", all_i)
