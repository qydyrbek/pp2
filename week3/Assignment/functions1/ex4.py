import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1,1):
        if x % 2 == 0:
            return False
    return True
n = int(input())
a = input().split()
for i in range(0,0,1):
    a[i] = int(a[i])
    if prime(a[i]) == True:
        print(a[i])