import traceback
#creating custom error
try:
  num=int(input("enter number:"))
  print(10/num)
except ValueError:
  print("enter only number")
except ZeroDivisionError:
  print("cannot divide by zero")
# ****************************************************
#create a custom error using class
class MarksError(Exception):#made my own error for mark
    pass

marks = 150

try:            #try = “I am expecting error”    #You cannot use try alone need to use except always
    if marks > 100:
        raise MarksError("Marks cannot be above 100")

except MarksError as e: #except = “What to do if error comes?” , 
    print(e)


#*******************************************************
#use of finally
try:
  num=int(input("enter number:"))
  print(10/num)
except ValueError:
  print("enter only number")
except ZeroDivisionError:
  print(" cant divided with zero")
finally:
  print("0000 program ended 000")#given error or not whenever the program is ending end with the execution of code under finally


#raise

# syntax: 
#  raise ExceptionType("error message")
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")

print(age)

#
num = 0

if num == 0:
    raise ZeroDivisionError("Zero not allowed")
