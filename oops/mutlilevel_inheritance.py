class Grandfather:
  def grandpa(self):
    return "i love my grandpaaa, he was a miltery officer"

class Father(Grandfather):
  def papa(self):
    return "my father is a business man"
  
class Mother(Father):
  def mom(self):
    return "my mom is a teacher , i love her"

class Child(Mother):
  def kid(self):
    return "my name is anshu"
  
c1=Child()
print("\n"+ c1.kid()+" "+c1.mom()+" "+c1.papa()+ " "+c1.grandpa())

