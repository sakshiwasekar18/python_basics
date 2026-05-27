# Encapsulation = hiding data and accessing it through methods

class BankAccount:
  def __init__(self):
    self.__balance = 0 #its a private variable

#getter method
  def get_balance(self):
    return self.__balance
  
  # setter method
  def deposite(self,amount):
    self.__balance+= amount

acc=BankAccount()
acc.deposite(1000)
print(acc.get_balance())


print("\n************student-marks******\n")
class Student:
  def __init__(self):
    self.__marks = 0

  def get_marks(self):
    return self.__marks
  
  def set_marks(self,marks):
    if 0< marks < 100:
      self.__marks+=marks

s=Student()
s.set_marks(89)
print(s.get_marks())

