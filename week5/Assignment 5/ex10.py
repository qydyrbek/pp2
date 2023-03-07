import re 

f = open("C:\Users\User\Desktop\pp2\week5\check.txt", "r")
result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', f)
print(result)