i = int(input())
prev = i
count = 1
max_count = 1
while i != 0:
    i = int(input())
    if prev == i:
        count += 1
    else:
        prev = i
        if max_count < count:
            max_count = count
        count = 1
print(max_count)

