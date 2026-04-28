print("welcome to atm_machine")
print()
while True:
  choice=int(input("enter the operation number you want to perform :[1.check balance, 2.deposite, 3.withdrawal] :"))
  balance=1000
  print()

  match choice:
    case 1:
      print(balance)
    case 2:
      deposite=int(input("enter the amount :"))
      balance=balance+deposite
      print(f"balance amount :{balance}")
    case 3:
      withdrawal=int(input("enter the amount: "))
      balance =balance-withdrawal
      print(f"balance amount :{balance}")
    case _:
      print("invalid request")
  choose=input("do you want to perform any other operation:(yes/no ):").strip().lower()
  if choose!="yes":
    print("thank you for visiting")
    break
