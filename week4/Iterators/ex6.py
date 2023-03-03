class sandar():
  def __iter__(self):
    self.a = 0
    return self 
    
  def __next__(self):
    if self.a <= 40:
      x = self.a 
      self.a = self.a + 2 
      return x
    else:
      raise StopIteration
    
    
san = sandar()
itera = iter(san)

for x in itera:
  print(x)