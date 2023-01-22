# Create a class called Rational for performing arithmetic with fractions. Write a program to test your class.
# Use integer variables to represent the private data of the class – the numerator and the denominator.
# Provide a init() method that enables an object of this class to be initialized when it’s declared. The init()
# should contain default parameter values in case no initializers are provided and should store the fraction in
# reduced form. For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in
# the denominator. Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        gcd = self.__gcd(numerator, denominator)
        self.__numerator = int(numerator / gcd)
        self.__denominator = int(denominator / gcd)

    def __gcd(self, x, y):  # find GCD - greater common divisor
        while(y):
            x, y = y, x % y
        return abs(x)

    def print_fraction(self):
        print(f"{self.__numerator}/{self.__denominator}")

    def print_floating(self):
        print(self.__numerator / self.__denominator)

x = Rational(4, 16)
x.print_fraction()
x.print_floating()

y = Rational(125, 300)
y.print_fraction()
y.print_floating()