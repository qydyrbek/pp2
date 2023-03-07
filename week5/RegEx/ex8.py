import re

txt = "Bailangan tilim soilemeidi"
x = re.sub("\s", "91", txt, 1)
print(x)
