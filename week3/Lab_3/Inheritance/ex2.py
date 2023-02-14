class kolik:
  def __init__(self, mark, model):
    self.mark = mark
    self.model = model 
    
  def print1(self):
    print(self.mark, self.model)
    
class machine(kolik):
  pass
    

x = machine('mitsubishi' , 'lancer')

x.print1()