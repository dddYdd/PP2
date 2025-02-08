#1
class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")
    
    def printString(self):
        print(self.input_string.upper())


string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()



#2
class Shape:
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

square = Square(4)
print("Area of the square:", square.area())  

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.area())  

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point2.show()  

point1.move(3, 4)
point1.show()  

distance = point1.dist(point2)
print("Distance between the points:", distance)  

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

account = Account("John", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  

#6
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 13, 21, 2, 8]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)




