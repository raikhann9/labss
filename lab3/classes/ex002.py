class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length=float(input())
    def area(self):
        return self.length**2

p1=Square()
print(p1.area())

