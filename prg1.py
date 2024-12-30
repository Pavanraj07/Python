from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def draw(self):
        return f"drawing a circle with radius {self.radius}"
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def draw(self):
        return f"drawing a circle with side {self.side}"
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height


    def draw(self):
        return f"drawing a circle with width {self.width} and height {self.height}"
    
class ShapeFactory:
    def create_shape(self,shape_type,*args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Square(*args)
        elif shape_type == "Rectangle":
            return Rectangle(*args)
        else:
            raise ValueError(f"unknown shape type:{shape_type}")

if __name__ == "__main__":
    factory = ShapeFactory()

    shapes = {
        factory .create_shape("Circle" ,5),
        factory .create_shape("Square" ,4),
        factory .create_shape("Rectangle" ,3 , 6)
    }
for Shape in shapes:
    print(Shape.draw())