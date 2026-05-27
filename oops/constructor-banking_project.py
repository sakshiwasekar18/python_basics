class BankAccount:
  def __init__(self,name,amount):
    self.name=name
    self.amount=amount

  def show_balance(self):
    print(f"your balance is {self.amount}")

  def deposite(self,deposite):
    self.amount+=deposite
    print(f"{deposite} deposited, \n your current balance is {self.amount}")

  def withdraw(self,withdraw):

    if withdraw > self.amount:
      print("insufficient balance ")
    else:
      self.amount -= withdraw
      print(f"{withdraw} withdrawded, \n your current balance is {self.amount}")

# If your constructor has parameters, you MUST pass arguments when creating object
b1=BankAccount("sakshi",10000)
b1.show_balance()

b1.deposite(900)

b1.withdraw(600)

b1.show_balance()


print("\n for another account \n ")
b2=BankAccount("isha",50000)
b2.show_balance()

b2.deposite(100)

b2.withdraw(800)

b2.show_balance()
