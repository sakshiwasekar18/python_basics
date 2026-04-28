#check the value is positive or negative
print("***check the value is positive or negative****")
num=int(input("enter a number:"))
if num>=0:
  print(f"{num} is a positive number")
else :
  print(f"{num} is a negative number")
  
  print()
#check the number is odd or even
print("***check the number is odd or even****")
num=int(input("enter a number :"))
if num%2==0:
  print("the given number is even")
else:
  print("the given number is odd")

print()
#greater num
print("********greater number between 2 numbers****")
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
  print("a is greater")
else:
  print("b is greater")

print()
#greater number betweem 3 number
print("********greater number between 3 numbers****")
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if a>b:
  print("a is greater")
elif b>c:
  print("b is greater")
else:
  print("c is greater")


print()
#three numbers are equale or not 
print("three numbers are equale or not ")
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
print()
if a==b:
  if b==c:
    print("given 3 numbers are equale")
else:print("numbers are not equale")

#voter age 
age = int(input("enter your age :"))
if age>=18:
  print("you are eligible to vote :")
else:
  print("you are underage")