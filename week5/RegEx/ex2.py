import re

txt = "Kazakhstan is the best"

x = re.findall("Almaty", txt)
print(x)

if (x):
  print("Iya bul jerde tym bolmaganda bir ret saikestik bar")
else:
  print("Saikestik joq")
