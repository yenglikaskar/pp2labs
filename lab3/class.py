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


#4 task
from math import sqrt

class Point:
    x0 = 0
    y0 = 0
    def __init__(self):
        self.x = int(input("x coordinate: "))
        self.y = int(input("y coordinate: "))

    def show(self):
        print(f"Point coordinates ({self.x}, {self.y})")

    def move(self):
        global x0, y0
        x0 = self.x
        y0 = self.y
        self.x = int(input("x coordinate: "))
        self.y = int(input("y coordinate: "))

    def dist(self):
        self.distance = sqrt((x0 - self.x) ** 2 + (y0 - self.y) ** 2)
        print("The distance between 2 points:", round(self.distance, 2))


point = Point()
point.show()
point.move()
point.dist()


# 5 task
class Account:
    def __init__(self):
        self.owner = input("Enter your name: ")
        self.balance = float(input("Enter your balance: "))

    def deposit(self):
        amount = float(input("Deposit: "))
        self.balance += amount
        print("Your balance: ", self.balance, "\n")

    def withdraw(self):
        amount = float(input("Withdraw: "))
        if amount > self.balance:
            print("You can not exceed the available balance.")
        else:
            self.balance -= amount
        print("Your balance: ", self.balance, "\n")

acc = Account()
acc.deposit()
acc.withdraw()


# 6 task
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filt_prime(nums):
    return list(filter(lambda x: is_prime(x), nums))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = filt_prime(numbers)
print("Prime numbers:", prime_numbers)          

