from datetime import datetime
  
start = datetime.strptime("2023-3-1 12:0:0" , '%Y-%m-%d %H:%M:%S')
end = datetime.strptime("2023-3-8 12:0:0" , '%Y-%m-%d %H:%M:%S')
  
difference = end - start
  
seconds = difference.total_seconds()
print(seconds)
