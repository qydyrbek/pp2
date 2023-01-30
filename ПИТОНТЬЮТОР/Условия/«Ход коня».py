a = int(input())
b = int(input())
x = int(input())
y = int(input())

if (abs(a-x) == 1 and abs(b-y) == 2) or (abs(a-x) == 2 and abs(b-y) == 1):
  print("YES")
else:
  print("NO")