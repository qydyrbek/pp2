N = int(input())
M = int(input())
x = int(input())
y = int(input())
a = max(M,N)
b = min(M,N)
c = min(x,y,b-x,a-y)
print (c)