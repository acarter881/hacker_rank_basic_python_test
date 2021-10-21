import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return (self.a * self.b)

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * (self.r ** 2)
