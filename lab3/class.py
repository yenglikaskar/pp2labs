class Two:
    def __init__(self):
        self.text = "" 
    
    def inputt(self):
        self.text = input()
        
    def change(self):
        if self.text:
            print(self.text.upper())
        else:
            print("error")


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2
a = int(input())
sq = Square(a)
print(sq.area())  



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

l = int(input())
w = int(input())

rect = Rectangle(l, w)
print("S = ", rect.area())

