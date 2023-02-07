x = int(input())
max = 0
i = -1
k = 0
while x != 0:
    i += 1
    if max < x:
        max = x
        k = i
    x = int(input())
print(k)
