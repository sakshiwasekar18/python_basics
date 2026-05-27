#same method name but it performs differently 
class dog:
  def sound(self):
    print("dog braks")
class cat:
  def sound(self):
    print("cat meows")

d=dog()
c=cat()
d.sound()
c.sound()