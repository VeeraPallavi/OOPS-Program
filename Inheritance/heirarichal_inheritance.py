class Shape:
    def display(self):
       print("This is a shape")

class Circle(Shape):
   def area(self):
      print("Area of circle")

class Rectangle(Shape):
   def area(self):
      print("Area of Rectangle")
    
circle = Circle()
circle.area()
circle.display()

rectangle = Rectangle()
rectangle.area()
rectangle.display()


