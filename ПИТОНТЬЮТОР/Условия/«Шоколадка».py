a = int(input())
b = int(input())
c = int(input())
d = a * b 

if d < c :
  print("NO")
elif c % a == 0 or c % b == 0:
  print("YES")
else:
  print("NO")