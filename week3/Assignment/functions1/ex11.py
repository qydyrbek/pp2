def polin(s):
    return s == s[::-1]
s = str(input())
str1 = polin(s)
if str1:
    print('Yes')
else:
    print('No')