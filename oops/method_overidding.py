# When a child class writes the same method as parent class to change its behavior
# Same method name
# Happens in inheritance
# Child replaces parent method


print("\n*********example animal-sound*******\n")

class Animal :
  def sound(self):
    print("animals makes sound")

class Dog(Animal):
  def sound(self):
    print("dog barks")
  
class Cat(Animal):
  def sound(self):
    print("cat meows")

a=Animal()
d=Dog()
c=Cat()

a.sound()
d.sound()
c.sound()

print("\n*****method overridding example**********,\n shapes and its area\n")

class Shape:
  def area(self):
    print("Area")

class Rectrangle(Shape):
  def area(self):
    l=8
    b=2
    print("rectrangle area:",l*b)

class Square(Shape):
  def area(self):
    s=5
    print("square area",s*s)

class Circle(Shape):
  def area(self):
    r=5
    print("Circle area",3.14*r*r)

s=Shape()
r=Rectrangle()
sq=Square()
c=Circle()

s.area()
r.area()
sq.area()
c.area()


print("\n ****example employee and their salary*****\n")
class Employee:

  def salary(self):
        print("Employee salary")


class Manager(Employee):

    def salary(self):
        print("Manager salary = 50000")


class Developer(Employee):

    def salary(self):
        print("Developer salary = 40000")


m = Manager()
d = Developer()

m.salary()
d.salary()

print("\n****example payment methods*****\n")

class Payment:
   def pay(self):
      print(" u can use tye following methods to amke a payment:")

class Cash(Payment):
   def pay(self):
      print("make payment using cash ")

class Card(Payment):
   def pay(self):
      print("make payment using card ")

class Upi(Payment):
   def pay(self):
      print("make payment using  Upi")

p=Payment()
c=Cash()
car=Card()
u=Upi()

p.pay()
c.pay()
car.pay()
u.pay()