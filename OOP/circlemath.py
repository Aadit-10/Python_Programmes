import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def cir(self):
        return 2 * math.pi * self.radius

    def change_radius(self, new_radius):
        self.radius = new_radius


circle = Circle(1)

while True:
    radius = float(int(input("Enter the radius :")))
    circle.change_radius(radius)
    print("Area:", circle.area())
    print("circumference ", circle.cir())
