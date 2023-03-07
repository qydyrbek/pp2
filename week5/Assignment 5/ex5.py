import re 

f = open("C:\Users\User\Desktop\pp2\week5\check.txt", "r")
result = re.findall(".*a.*b$", f.read())
print(result)