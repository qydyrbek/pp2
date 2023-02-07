def myfunc(x):
  fc = 1
  for x in range(1 , x + 1):
    fc = fc * x 
  return fc
  
n = int(input())
fac = 0
for x in range(1, n + 1):
  fac = fac + myfunc(x)
  
print(fac)