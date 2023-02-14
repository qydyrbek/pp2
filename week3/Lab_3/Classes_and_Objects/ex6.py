class kolik:
  def __init__(self, mark, model):
    self.mark = mark 
    self.model = model 
    
  def func(self):
    print("bul kolikting aty " + self.mark)
   
   
p = kolik("toyota" , "supra")

p.func()