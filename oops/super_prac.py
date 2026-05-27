#super key =super() is used to call methods from the parent class
#example parent-child
print("\n  **********example parent-child ******************")

class Parent:
  def parFun(self):
    print("Parent")

class Child(Parent):
  def childFun(self):
    super().parFun()
    print("Child")

c = Child()
c.childFun()

#example to practice super keyword 
print("\n ******example student info ********")
class Record:
  
  def info(self):
    self.name=input("enter a name: ")

class getInfo(Record):
  def get(self):
    super().info()
    print(self.name +" is a good student")

c1=getInfo()
c1.get()

print("\n********************example car************")
#super() → used to call parent class's method in inheritance chain
class Car:
  def car_brand(self):
    print("toyata is a nice car")

class car2:
  def car_colour(self):
    print("car colour is black ")

class car3:
  def car_speed(self):
    print("car speed is 120km/hr")

class print_info(Car,car2,car3):
  def get_info(self):
    # super().car_brand()
    # super().car_colour()
    # super().car_speed()# this wroks but dont do this use irt like this 

    self.car_brand()
    self.car_colour()
    self.car_speed()

c3=print_info()
c3.get_info()

    