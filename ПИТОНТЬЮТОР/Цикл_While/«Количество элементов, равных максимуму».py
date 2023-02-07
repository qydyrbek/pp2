a = int(input())
k = 0
c = 0
while a!=0:
    if k < a:
        k=a
        c=1
    elif k == a:
        c+=1
    a = int(input())
print(c)