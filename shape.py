class Shape:

    def __init__(self,name):
        self.name = name
    
    def get_area(self):
        return self.area
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def get_area(self):
        area = 3.14 * self.radius **2
        print(area) 
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def get_area(self):
        area = self.width * self.length
        print(area)
    
my_circle = Circle(3)
my_circle.get_area(my_circle)


my_rectangle = Rectangle(2,2.3)
my_rectangle.get_area(my_rectangle)
