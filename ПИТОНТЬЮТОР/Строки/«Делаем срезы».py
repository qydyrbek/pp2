a = str(input())
print(a[2])
print(a[-2])
print(a[:5])
print(a[:len(a)-2])
nech = ""
ch = ""
for x in range(0, len(a)):
  if x % 2 == 1:
    nech = nech + a[x]
  else:
    ch = ch + a[x]

print(ch)    
print(nech)
print(a[::-1])
print(a[::-2])
print(len(a))
