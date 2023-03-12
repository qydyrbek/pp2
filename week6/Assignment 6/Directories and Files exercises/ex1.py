import os

f="C:\\Users\\User\\Desktop\\pp2\\week6"
for root, directories, files in os.walk(f):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)