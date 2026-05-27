#Same method name Different number/type of arguments

class Maths:
  def add(self,a=0,b=0,c=0):
    print(a+b+c)

m=Maths()
m.add(2,3)
m.add(2,3,7)


print("\n ******area and shapes**** *\n")

class Area:
  def shapes(self,a=None,b=None):
    if a and b:
      print("area of Rectraingle :",a*b)
    elif a:
      print("area of Square :" ,a*a)

    else:
      print("no values")
   

a=Area()
a.shapes(3)
a.shapes(3,8)
a.shapes(3,8)

print("\n**** student details*\n")

class student:
  def info(self,Name=None,Age=None):
    if Name and Age:
      print(f"Name:{Name},\n Age:{Age}")

    elif Name:
      print(f"my name is {Name}")

    else:
      print("no data recived")

s=student()
s.info("sakshi",23)
s.info(23)  #see this gives error 
s.info("sakshi")

class Student:
    def info(self, data=None):
        if data:
            name = data.get("name")
            age = data.get("age")

            if name and age:
                print(f"Name: {name}, Age: {age}")
            elif name:
                print(f"My name is {name}")
            else:
                print("No data received")
        else:
            print("No data received")


s = Student()

s.info({"name": "sakshi", "age": 23})
s.info({"name": "sakshi"})
s.info({})


class Student:
    def info(self, name=None,age=None):
        
            if name and age:
                print(f"Name: {name}, Age: {age}")
            elif name:
                print(f"My name is {name}")
            else:
                print("No data received")
        


s = Student()

s.info(32,"isha")
s.info(age=32,name="sakshi")
s.info()


class Salary:

    def calculate(self, basic, bonus=0):
        print("Total Salary =", basic + bonus)


s = Salary()

s.calculate(20000)
s.calculate(20000, 5000)