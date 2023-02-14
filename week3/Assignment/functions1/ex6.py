def func(str1):
  list1 = str1.split(" ")
  list1.reverse()
  emp_str = ""
  for x in list1:
    emp_str = emp_str + " " + x 
  print(emp_str.strip())

str1 = str(input())
  
func(str1)