ch = 0
a = int(input())
cnt = 0
while a != 0:
    if a % 2 == 0:
      cnt = cnt + 1
    a = int(input())
    
print(cnt)