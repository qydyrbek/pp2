import math

n = int(input())
s = int(input())

area = (n * pow(s,2)) / (4 * math.tan(math.pi / n))

print(area)