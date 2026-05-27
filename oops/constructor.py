# A constructor is a special method that:
# runs automatically when an object is created
# is used to initialize (set up) data inside the object




print("------------------- student-------------------")


class student:
  # Constructor → runs automatically when object is created
    
  def __init__(self,name,age):
    #storing variable inside the object
    self.name=name #object variable 
    self.age= age   #object variable 

  def show(self):
    print(self.name,self.age)

# creating object → constructor is called here automatically
s1=student("sakshi",21)
s1.show()




print("------------------- CAR -------------------")

class car:
  def __init__(self,car_name,colour,price):
    self.car_name = car_name
    self.colour=colour
    self.price=price 
  
  def show_details(self):
    print(f"brand:{self.colour}")
    print(f"car_name:{self.car_name}")
    print(f"price:{self.price}")

  def applydiscount(self,percent):
    dis_ammount=(percent/100)*self.price
    self.price-=dis_ammount
    print(f"price after discount of {percent}% is {self.price}")

c1=car("bmw","black",1200000)

c1.show_details()
c1.applydiscount(10)


#****************note**************
#  def always creates a function
# BUT… If that function is inside a class, we call it a method


