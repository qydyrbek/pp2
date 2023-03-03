x = 30
def func():
  global x
  x = 20
  print(x)
  
func()

print(x)
