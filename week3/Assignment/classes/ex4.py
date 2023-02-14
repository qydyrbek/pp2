class Point:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def show(self):
        print(f"Coordinate: {self.x1},{self.x2}")
    
    def move(self, nx, ny):
        self.x1 += nx
        self.x2 += ny

    def dist(self, inner):
        d = (abs(self.x1 - inner.x1)**2 + abs(self.x2 - inner.x2)**2) ** (1/2)
        print(f"Distance: {d}")

poi = Point(2, 6)
poi.show()
poi.move(10, 10)
poi.show()
poi2 = Point(0, 0)
poi2.show()
poi.dist(poi2)