class shape:
    def __init__(self):
        pass

    def area(self):
        return 0
        
class rect(shape):
    def __init__(self , length , wedth):
        super().__init__()
        self.sz=length
        self.cz=wedth

    def area(self):
        return self.sz*self.cz

a = int(input())
b = int(input())
j = rect( a , b )
print(j.area())