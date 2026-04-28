#solved by using case
#their are 7 arethematic operators
math=input("enetr the arethematic operation you want to perform:")
print()
a=int(input("enter a number: "))
b=int(input("enter a number: "))
print()
match math:
  case "+":
    print(a+b)
  case "-":
    print(a-b)
  case "*":
    print(a*b)
  case "/":
    print(a/b)
  case "//":
    print(a//b)
  case "%":
    print(a%b)
  case "**":
    print(a**b)
  case _:
    print("error")
