def func(n):
  return lambda a : a * n
  
san = func(5)

print(san(15))