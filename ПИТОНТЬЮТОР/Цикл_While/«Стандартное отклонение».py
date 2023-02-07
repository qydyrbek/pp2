from math import sqrt
x=-1
z=0
y=0
w=0
while x!=0:
    x=int(input())
    z+=1
    w+=x
    y+=x**2
print(sqrt((y-w**2/(z-1))/(z-2)))
