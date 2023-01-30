a = int(input())
b = int(input())
x = int(input())
y = int(input())

if (abs(x-a) == abs(y-b)) or x == a or y == b:
  print("YES")
else:
  print("NO")