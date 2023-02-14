def func(n):
  return lambda a : a * n
  
ush_ese = func(3)
eki_ese = func(2)

print(ush_ese(20))
print(eki_ese(20))