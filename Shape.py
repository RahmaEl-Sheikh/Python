#Q12&Q13

import math
class Shape:
    color=""
    def area(self):
        pass  

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi) * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


c = Circle(7)
print("Circle area:", c.area()) 

r = Rectangle(7, 3)
print("Rectangle area:", r.area()) 