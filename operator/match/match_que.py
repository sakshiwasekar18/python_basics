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

#days by number
day=int(input("enter the number for a day:"))
match day:
  case 1:
    print("monday")
  case 2:
    print("tuesday")
  case 3:
    print("wednesday")
  case 4:
    print("thusday")
  case 5:
    print("friday")
  case 6:
    print("saturday")
  case 7:
    print("sunady")
  case _:
    print("invalid input")