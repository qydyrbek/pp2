n = int(input())
arr = []
for x in range(0 , n ):
  a = str(input())
  arr.append(a)
  

def func(arr):
  global cnt
  cnt = 0
  for x in range(0 , n-1 ):
    if arr[x] == "0" and arr[x+1] == "0" and arr[x+2] == "7":
      cnt = cnt + 1 
  print(bool(cnt))  
  
func(arr)