
# ================== ENCAPSULATION IN PYTHON ==================

# DEFINITION:
# Encapsulation means wrapping data (variables) and methods (functions)
# together into a single unit (class), and restricting direct access to data.
# -> Keeping data (variables) and functions (methods) together in one class
# -> And NOT allowing direct access to data
# -> Hide data and use methods to access it
# In simple words:
# -> Encapsulation = "Data Hiding + Controlled Access"


# ------------------ WHY ENCAPSULATION? ------------------

# 1. To protect sensitive data (like PIN, balance)
# 2. To prevent accidental changes
# 3. To control how data is accessed or modified
# 4. To make code more secure and organized

# ------------------ TYPES OF ACCESS MODIFIERS ------------------

# 1. PUBLIC
# -> Accessible from anywhere (inside class, outside class, any file)
# -> No underscore is used
# self.name = "sakshi"


# 2. PROTECTED
# -> Meant to be used inside class and child classes (inheritance)
# -> Represented using a single underscore (_)
# self._balance = 1000


# 3. PRIVATE
# -> Accessible only inside the same class
# -> Represented using double underscore (__)
# -> Python performs name mangling to restrict access
# self.__pin = "1234"


# ------------------ HOW ENCAPSULATION IS ACHIEVED ------------------

# We use methods to control access:

# 1. Getter Method -> Used to read data
# 2. Setter Method -> Used to modify data

# Example:
# def get_balance(self):
#     return self._balance

# def set_balance(self, amount):
#     self._balance += amount


# ✔ Encapsulation improves:
#    - Security
#    - Maintainability
#    - Code structure

# ================== END ==================



print("\n***********ATM-ENCAPSULATION-PROJECT***********\n")

class ATM:
    def __init__(self, name):
        self.HolderName = name        # 🔓 PUBLIC (accessible anywhere)
        self._balance = 10000         # 🟡 PROTECTED (internal use)
        self.__pin = "123"            # 🔒 PRIVATE (hidden)

    # 🔒 Encapsulation: accessing private data via method
    def verify_pin(self, pin):
        return pin == self.__pin

    # 🔒 Controlled access to withdraw
    def withdraw(self, pin, amount):
        if self.verify_pin(pin):   # accessing private via method
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdraw successful. Balance: {self._balance}")
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")

    # 🔒 Controlled access to deposit
    def deposit(self, pin, amount):
        if self.verify_pin(pin):
            self._balance += amount
            print(f"Deposit successful. Balance: {self._balance}")
        else:
            print("Wrong PIN")

    # ✅ Getter method (proper encapsulation)
    def get_balance(self, pin):
        if self.verify_pin(pin):
            return self._balance
        else:
            return "Access Denied"

    # ✅ Setter-like control (optional improvement)
    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("Wrong old PIN")


class HomePage:
    def welcome(self):
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        return name, pin


# ------------------ MAIN FLOW ------------------

h = HomePage()
name, pin = h.welcome()

atm = ATM(name)

atm.deposit(pin, 500)
atm.withdraw(pin, 200)

# 🔥 Encapsulation here:
# Instead of accessing atm._balance directly ❌
# we use method get_balance() ✅

print("Balance:", atm.get_balance(pin))

atm.change_pin(pin, "999")




#self made --------------------------------------------------------------

# print("\n***********ATM-project******\n")


# class ATM:
#   def __init__(self,Name):
#     self.HolderName = Name #public
#     self._balance=10000 #protected
#     self.__pin="123" #private

#   def withdraw(self,pin,amount):
#     if pin==self.__pin:
#       if amount < self._balance:
#         self._balance-=amount
#         print(f" your Account Balance is {self._balance}")
#       else:
#         print("insufficient balance")
#     else:
#       print("wrong pin")

#   def deposit(self,pin,amount):
#     if pin==self.__pin:
#       self._balance+=amount
#       print(f" your Account Balance is {self._balance}")
#     else:
#       print("wrong pin")

# class HomePage:
#   def Welcome(self):
#     Name=input("enter your name: ")
#     pin=input("enter your pin: ")
#     return Name ,pin

# class Balance:
#   def get_balance(self,obj):
#     return obj._balance
  


# h=HomePage()
# Name,pin =h.Welcome()

# a=ATM(Name)
# a.withdraw(pin,20)
# a.deposit(pin,100)

# b=Balance()
# print("balance:",b.get_balance(a))

