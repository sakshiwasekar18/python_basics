#  inheretance- One class takes properties (methods/variables) from another class

#inheritance parent-child example
print("\n ******inheritance parent-child example******\n")
class Parent:
  def Parent_1(self):
    print("hello, i am parent")

class Child(Parent):
  def Child_1(self):
    print("i am child")

c1=Child()
c1.Child_1()
c1.Parent_1()



#inheritance animal-sounds example
print("\n *******inheritance animal-sounds example****\n ")


class Animal:
  def Animal_1(self):
    print("i am a dog ")

class Sound(Animal):
  def Sound_1(self):
    print("i bark")

c2=Sound()
c2.Sound_1()
c2.Animal_1()



#vehical-colour example
print("\n ******vehical-colour example")

class Vehical:
  def Car(self):
    print("BMW")

class Colour(Vehical):
  def Colour_1(self):
    print("black")
    
c3=Colour()
# c3.Car()
# c3.Colour_1()

c3.Colour_1()
c3.Car()


#(********conceptUAL*********)
print("\n ************example as how to use method of one class into another ")

class Sentence:
  def sen1(self):
    return "life is good"

class join(Sentence):
  def sen2(self):
    return "i am so happy to have it"

c4=join()
print(c4.sen1()+" "+ c4.sen2())
