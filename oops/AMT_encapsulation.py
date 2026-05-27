
print("\n***********bank-project******\n")

class ATM:
  def __init__(self,Name):
    self.HolderName = Name #public
    self._balance=10000 #protected
    self.__pin="123" #private

  def withdraw(self,pin,amount):
    if pin==self.__pin:
      if amount < self._balance:
        self._balance-=amount
        print(f" your Account Balance is {self._balance}")
      else:
        print("insufficient balance")
    else:
      print("wrong pin")

  def deposit(self,pin,amount):
    if pin==self.__pin:
      self._balance+=amount
      print(f" your Account Balance is {self._balance}")
    else:
      print("wrong pin")

class HomePage:
  def Welcome(self):
    Name=input("enter your name: ")
    pin=input("enter your pin: ")
    return Name ,pin

class Balance:
  def get_balance(self,obj):
    return obj._balance
  


h=HomePage()
Name,pin =h.Welcome()

a=ATM(Name)
a.withdraw(pin,20)
a.deposit(pin,100)

b=Balance()
print("balance:",b.get_balance(a))

