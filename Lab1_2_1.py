# Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter 
# and the area of the rectangle. Also, provide setter and getter for the length and width attributes. The setter should verify that 
# length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    def __init__(self, _length = 1, _width = 1):
        self._length = _length
        self._width = _width

    def get_length(self):      # length getter
        return self._length

    def get_width(self):       # width getter
        return self._width

    def set_length(self, l):   # length setter
        if (l < 20.0 and l > 0.0):
            self._length = l
        else:
            print("Length out of range!")

    def set_width(self, w):    # width setter
        if (w < 20.0 and w > 0.0): 
            self._width = w
        else:
            print("Width out of range!")

    def perimeter(self):
        return (2 * self._length + (2 * self._width))

    def area(self):
        return (self._length * self._width)

ABCD = Rectangle()
BCDA = Rectangle()

ABCD.set_length(10)
ABCD.set_width(14)

BCDA.set_length(100)

print(ABCD.perimeter(), ABCD.area())
print(BCDA.perimeter(), BCDA.area())