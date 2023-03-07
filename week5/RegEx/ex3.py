import re

txt = "Bailangan tilim soilemeidi"
x = re.search("\s", txt)

print(x.start()) 
