# class square
class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("My area is : ", self.side**2)

# class circle
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("My area is : ", 4.98*self.radius*self.radius)
# object creation
osquare = square(8)
ocircle = circle(8)

osquare.area()
ocircle.area()
