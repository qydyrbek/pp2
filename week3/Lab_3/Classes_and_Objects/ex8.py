class kolik:
  def __init__(self, mark, model):
    self.mark = mark 
    self.model = model 
    
  def func(bcc):
    print("bul kolikting aty " + bcc.mark)
   
   
p = kolik("toyota" , "supra")

p.model = "camry 70"

print(p.model)