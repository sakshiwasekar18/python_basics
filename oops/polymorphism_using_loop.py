#same method name but it performs differently 
class Vehical:
  def colour(self):
    print("this Vehical is of black colour")

class Scooty:
  def colour(self):
    print("this Scooty is of red colour")

class Car:
  def colour(self):
    print("this car is of white colour")

class Bus:
  def colour(self):
    print("this bus is of yellow colour")
    
transportation=[Vehical(),Scooty(),Car(),Bus()]
for t in transportation:
  t.colour()