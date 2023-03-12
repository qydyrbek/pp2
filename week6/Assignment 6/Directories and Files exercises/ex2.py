import os

print('Exist:', os.access("C:\\Users\\User\\Desktop\\pp2\\week6", os.F_OK))
print('Readable:', os.access("C:\\Users\\User\\Desktop\\pp2\\week6", os.R_OK))
print('Writable:', os.access("C:\\Users\\User\\Desktop\\pp2\\week6", os.W_OK))
print('Executable:', os.access("C:\\Users\\User\\Desktop\\pp2\\week6", os.X_OK))