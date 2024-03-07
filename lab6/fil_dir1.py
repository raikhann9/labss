#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path_ = r"D:\PP2"
all_i=os.listdir(path_)
for i in all_i:
    if os.path.isdir(os.path.join(path_, i)):
        direcs=i
    if os.path.isfile(os.path.join(path_, i)):
        filess=i

print("directories:", direcs)
print("files:", filess)
print("all items:", all_i)
