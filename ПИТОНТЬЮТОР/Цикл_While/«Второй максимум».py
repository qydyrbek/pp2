b=0
m=0
while True:
    n=int(input())
    if n==0:
        break
    if n>m:
        b=m
        m=n
    elif n>b:
        b=n
print(b)
