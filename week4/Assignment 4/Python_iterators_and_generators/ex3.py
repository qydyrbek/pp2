def div(n):
    for i in range(1,n+1,1):
        if i%3==0 and i%4==0:
            print(i)

div(int(input()))

n=int(input())
a=[i for i in range(0,n+1,1) if i%12==0]
print(a)