import os

path = "C:\\Users\\User\\Desktop\\pp2\\week6"
if os.path.exists(path):
    os.remove(path)
else:
    print('File does not exist')