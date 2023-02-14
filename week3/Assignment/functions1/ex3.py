def solve(headnum, legnum):
  y = (legnum - (2 * headnum))/2
  x = headnum - y
  print(str(x) + " chickens")
  print(str(y) + " rabbits")

headnum = int(input())
legnum = int(input())

solve(headnum , legnum)