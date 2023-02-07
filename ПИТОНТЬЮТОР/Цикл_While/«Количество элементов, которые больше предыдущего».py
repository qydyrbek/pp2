n = int(input())
x = 0
y = 0
while n != 0 :
    if x < n :
        y += 1
    x = n
    n = int(input())
print(y-1)
