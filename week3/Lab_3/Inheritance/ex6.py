class kolik:
  def __init__(self, mark, model):
    self.mark = mark
    self.model = model 
    
  def print1(self):
    print(self.mark, self.model)
    
class machine(kolik):
  def __init__(self, mark, model, year1):
    super().__init__(mark, model)
    self.year = year1
    
x = machine('mitsubishi' , 'lancer', 2019)
print(x.year)