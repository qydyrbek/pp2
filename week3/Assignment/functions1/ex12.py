n = int(input())
arr = []
for x in range(0 , n ):
  a = int(input())
  arr.append(a)

str = ""
cnt = 0
def func(arr):
  for x in range(0 , n ):
    str = " "
    for i in range(0, arr[x]):
      str = str + "*"
    print(str)
    
func(arr)