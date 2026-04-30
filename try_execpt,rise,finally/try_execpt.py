import traceback
# 1. Try - Except :Meaning
# Used to handle errors in program.
# try block → risky code
# except block → runs if error comes
# Syntax
# try:
#     code
# except:
#     code


# #types of errors
#ValueError
'''num=int(input("enter a number: "))
try:
  
  for i in range(1,11):
    print(f"{num} X {i}={num*i}")
except ValueError as e:
  if not num.isdigit():
    traceback.print_exc()'''#wrong because if u enter acb, the error that occur is not due to the execpt but due to only num statement the try and except never runs
#correct method

try:
    num = int(input("enter a number: "))
    
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

except ValueError:
    print("Invalid input! Please enter a number.")

#KeyError
try:
    data={"name":"sakshi",
          "number":"33434"}
    print(data["age"])# dictionary does not have "age" key → error
except KeyError:
    traceback.print_exc()

#NameError
try:
    print(x)# variable x is not defined
except NameError:
    traceback.print_exc()

#ZeroDivisionError

try:
    num = int(input("Enter number: "))# division by zero
    a = 10 / num
    print(a)
except ZeroDivisionError:
    
    traceback.print_exc()
    print("Can't divide by zero")

#index
try:
    arr = [10, 20, 30]
    print(arr[5])# accessing invalid index
except IndexError:
    traceback.print_exc()

#TypeError
try:
    result = "10" + 5 # wrong data types used together
    print(result)
except TypeError:
   
    traceback.print_exc()
    print("This is a type error")

#FileNotFounderror
try:
    file = open("uuuu.txt")# file does not exist
except FileNotFoundError:
    traceback.print_exc()

#. ***********Multiple exceptions***********
# handles more than one error type
try:
    num1 = int(input("Enter number: "))# may cause ValueError if entered an string and so, it may give Value error
    print(num1)
    
    num = "10" + 5   # error comes here its a TypeError

except (ValueError, TypeError):
    traceback.print_exc()
#****************Exception:  catches ANY error *******
# You want to catch any kind of error You don’t know exact error type
try:
  num=int(input("enter a number:"))
  print(num)
except Exception:
  traceback.print_exc()
#note :
'''Exception → built-in  class → no import needed ✅
traceback → module → must import ✅
Prefer specific exceptions over general one(Exception)'''

'''ValueError → wrong input ,say we want int and user gave string 
ZeroDivisionError → divide by 0
NameError → variable missing,variable not defined say u used variable x but x is not defined
TypeError → wrong data types, wrong types used together
IndexError → list index wrong
KeyError → dictionary key wrong
FileNotFoundError → file missing
Exception → catches all'''