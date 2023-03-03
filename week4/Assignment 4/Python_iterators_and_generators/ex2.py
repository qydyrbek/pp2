def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
gen = even(n)

print(n)
for num in gen:
    if num == n:
        print(num)
    else:
        print(num)
