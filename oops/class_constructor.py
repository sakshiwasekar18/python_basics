#class example mobile ----------------
class mobile:
  #method 
  def show_details(self):
    print("brand:",self.brand)
    print("model_no:",self.model_no)

  #creating an object
m1=mobile()
  
  #assignment values 
m1.brand="realme"
m1.model_no="123dcf"

  #calling method 
m1.show_details()

#example student -------------------

class student:
  def student_info(self):
    print(f"name:{self.name}")
    print(f"age:{self.age}")
m2=student()

m2.name="samiksha"
m2.age=21

m2.student_info()

#example fruit ---------------------
class fruit:

#making a function 
  def fruit_name(self,name,colour):
    print(f"name:{name}")
    print(f"age:{colour}")

#making object 
m3=fruit()

#pass argument in the calling of the method 
m3.fruit_name("orange","orange ")

#example party ----------------------
class party:
  def arangment(self):
    print(f"name:",self.name)
    print(f"age",self.age)
    
m4=party()
m4.name="sakshi"
m4.age=21

m4.arangment()

# example marks class------------------------
class marks:
  def marks1(self,maths,sql,python):
    print(f" maths:{maths},\n sql:{sql},\n python:{python}")
m5=marks()
m5.marks1(34,56,78)


