import re

txt = "Suretterge o'n jetpeidi me keide?"
x = re.search(r"\bS\w+", txt)
print(x.string)
