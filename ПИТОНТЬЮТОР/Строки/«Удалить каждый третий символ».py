a = str(input())
nov = ""
for x in range(0 , len(a)):
  if x % 3 != 0:
    nov = nov + a[x]
    
print(nov)
