import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    
    def move(self):
        a=int(input())
        b=int(input())
        self.x+=a
        self.y+=b
        return self.x, self.y

    def dist(self):
        pointx=int(input())
        pointy=int(input())
        x1=self.x-pointx
        y1=self.y-pointy
        return math.sqrt(x1**2 + y1**2)

x=int(input())
y=int(input())
p1=Point(x, y)
print(p1.show())
print(p1.move())
print(p1.dist())



    