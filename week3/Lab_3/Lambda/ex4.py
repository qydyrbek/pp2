def func(n):
  return lambda a : a * n
  
san = func(4)

print(san(15))