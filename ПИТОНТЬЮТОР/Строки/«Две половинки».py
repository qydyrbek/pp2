x = input()
s = (len(x) + 1) // 2 
x1 = x[:s]
x2 = x[s:]
y = x2 + x1
print(y)
