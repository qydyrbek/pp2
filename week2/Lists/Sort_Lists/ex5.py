def myfunc(n):
  return abs(n-50)
  
sandar = [52, 6, 65, 9, 56]
sandar.sort(key = myfunc)
print(sandar)