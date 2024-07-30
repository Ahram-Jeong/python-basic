class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return (self.radius**2) * self.pi

    def perimeter(self):
        return 2 * self.radius * self.pi

    def multiply_radius(self, number):
        self.radius = self.radius * number
        print(f"Radius has been changed to {self.radius}")

mycircle = Circle(radius = 20)
print(mycircle.radius) # 20

mycircle2 = Circle(radius = 4)
print(mycircle2.area()) # 50.24
print(mycircle2.perimeter()) # 25.12

mycircle3 = Circle(4)
mycircle3.multiply_radius(20)
print(mycircle3.radius) # 80