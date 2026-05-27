#Abstraction = hiding implementation, showing only functionality

from abc import ABC, abstractmethod #you always have to import this to use abstration

print("\n********** student-marks **********\n")

class Student(ABC):
  @abstractmethod
  def info(self):
    pass

class Marks(Student):
  def info(self):
    print("ayush scored 99")

c=Marks()
c.info()

print("\n********** shape-area **********\n")
class Shape(ABC):
  def area(self):
    pass

class Area(Shape):
  def __init__(self,l,b):
    self.l=l
    self.b=b
    
  def area(self):
      print(f"area of the rectriangle is :{self.l*self.b}") 


a=Area(2,3)
a.area()


print("\n********** payment methods**********\n")
class Payment(ABC):
  def method(self,amount):
    
    pass

class Card(Payment):
  def method(self,amount):
    print(f"rs.{amount} payed sucessfully")

class Upi(Payment):
  def method(self,amount):
    print(f"rs.{amount} payed sucessfully")


class Cash(Payment):
  def method(self,amount):
    print(f"rs.{amount} payed sucessfully")

c=Card()
csh=Cash()
u=Upi()


c.method(9000)
csh.method(80)
u.method(10000)