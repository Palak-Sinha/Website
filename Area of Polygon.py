class Polygon:
    def __init__(self, sides):
        self.sides = sides
        

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(4)
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

if __name__ == '__main__':
    shapes = [Triangle(15, 20), Rectangle(28, 16), Square(22)]
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__} is {shape.area()}")







