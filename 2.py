from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print('L*H')
class Square(Rectangle):
    def area(self):
        print('L*L')

rectangleObj = Rectangle();
squareObj = Square();

rectangleObj.area();
squareObj.area();

# example of decorator

def square(func):
    def inner(x):
        return x * x
    return inner

@square
def num(a):
    return a

print(num(5))