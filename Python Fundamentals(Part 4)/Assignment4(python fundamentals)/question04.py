class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(3.14 * self.r * self.r)    

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print(f"area = {self.l * self.w}") 


class Trangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(f"area = {0.5 * self.b * self.h}")

