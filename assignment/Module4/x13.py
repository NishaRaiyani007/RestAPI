class circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = circle(5)
print(circle.area())
