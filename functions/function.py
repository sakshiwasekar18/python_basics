'''def my_fuction():
  print(" fuction just print example ")
my_fuction()

#fahrenheit to celsius 
def farhenheit(far):
   return (far-32)*5/9
print(farhenheit(90))

#different way to solve the same f to c take user input 
def farhenheit_to_celsius():
   farh=int(input("enter the value u want in celsius: "))
   far=(farh-32)*5/9
  
   return far
print(farhenheit_to_celsius())

#different way to solve the same f to c take user input 
def farhenheit_to_celsius():
   farh=int(input("enter the value u want in celsius: "))
   far=(farh-32)*5/9
   print(f"your value in celsius is :{far}")
   
farhenheit_to_celsius()

#return difference important ******************************************
def farhh():
   far=int(input("enter the value you want in c:"))
   far1=(far-32)*5/9
   print(f" your value is {far1}")
   return far1
farhh()
print(farhh())

#variable use in fucgtion 
def name():
   return "hello friend"
message=name()
print(message)

#variable use in fucgtion 
def name(name1):
   print("hi "+ name1)

message=name("sakshi")
print(message)



#ARGUMENTS
#print name by concat
def my_name(name):
   print("my name is "+ name)

my_name("sakshi")
#print name usinf f string
def my_name(name):
   print(f"my name is {name}")

my_name("sakshi")


#default parameter values :if a function is called without a parameter it will use the default value
#print names 

def name1(name="friend"):
   print("hi "+ name)
   print("hi", name)

name1("sakshi")

#keyword arguments

def sentence(name,day,mood):
   print(f"my name is {name},and its {day} today,i am feeling {mood}")

name=input("whats  your name: ")
day =input("whats the day today: ")
mood=input("how is your mood: ")
day=input(print("whats  todays day: "))
mood=input(print("how is your mood: ")) wrong way 

sentence(name,day,mood)
print()

#positional argument should be in order

def sentence1(animal,name,owner):
   return f"this is a {animal},its name is {name},its owner is {owner}"
print(sentence1("cat","kurri","sakshi"))'''

print()

def sentence1(animal,name,owner):
   return f"this is a {animal},its name is {name},its owner is {owner}"
print(sentence1(name="kurri",animal="cat",owner="sakshi"))


