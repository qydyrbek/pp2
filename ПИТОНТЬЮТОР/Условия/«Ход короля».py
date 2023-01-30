a = int(input())
b = int(input())
x = int(input())
y = int(input())

if (a-1 == x or a+1 == x or a == x) and (b-1 == y or b == y or b+1 ==y):
  print("YES")
else:
  print("NO")