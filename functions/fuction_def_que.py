#factorial of a number
def factorial():
  fact=int(input("enter the number whoes factorial you want :"))
  fac=1
  for i in range (1,fact+1):
    fac=fac*i
  print(f"you factorial for {fact} is {fac}")

factorial()

print()
#even number
def prime():
  num=int(input("enter the number range till which you want a even number:"))
  for i in range(0,num+1,2):
    print(i)
prime()

print()
#sum of two numbers
def sum():
  num1=int(input("enter a number:" ))
  num2=int(input("enter a number:" ))
  sum1=num1+num2
  print(f"sum of given numbers is {sum1}")
sum()

#sum by passing parameter and argument
def sum(num1,num2):
  sum1=num1+num2
  print(sum1)
sum(9,10)

#sum by positional
def sum_arg(n1,n2,n3):
  sum=n1+n2+n3
  print(sum)
sum_arg(n3=9,n2=3,n1=4)

print()
#prime number **************************************************************
def find_prime(num):
  if num <=1:
    return "not prime"
  for i in range(2,num):
    num%i==0
    return "not prime"
  return "prime"
print(find_prime(9))


