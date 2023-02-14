class shape:
    def __init__(self,num):
        self.num = num
    def area(self):
        return 0
class square(shape):
    def __init__(self , num):
        super().__init__(num)
        self.num = num
    def area(self):
        return self.num * self.num

a = int(input())
j = square(a)
print(j.area())