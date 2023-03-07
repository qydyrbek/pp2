import re 

f = open("C:\Users\User\Desktop\pp2\week5\check.txt", "r")
result = re.findall("[A-Z]+[a-z]+", f.read())
print(result)