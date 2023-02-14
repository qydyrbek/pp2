class kolik:
  def __init__(self, mark, model):
    self.mark = mark 
    self.model = model 
   
  def __str__(self):
    return f"{self.mark}({self.model})"
        
p = kolik("toyota" , "supra")

print(p)