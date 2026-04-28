#print number from 1 to 10
for i in range (1,11):
  print(i)

print()
#print even number upto 20
for j in range (2 ,20,2):
  print(j)
print()

'''for j in range (2 ,20):
  if(j%2==0):
    print(j)
print()'''

#print 0dd number upto 20
for j in range (1 ,20):
  if(j%2!=0):
    print(j)
print()
'''
for j in range (1 ,20,2):
  print(j)
print()'''

#print sum of 1st 10 natural numbers
sum1=0
for i in range (10):
  sum1=sum1+i
print(sum1)
print()

#print table of 2
print("table of two")
for i in range (1,11):
  print(f"2x{i}=",(2*i))

print()
#print table of 5
print("table of five")
for i in range (1,11):
  print(f"5x{i}=",(5*i))
print()

#print reserve counting from 1 to 10 
for i in range(10,0,-1): 
  print(i)
  print()
#done by while 
i=10
while (i>=1):
  print(i)
  i-=1

#print count of the entered number 
count1=input("enter as any numbers you want i'll give u the  total count:")
print(len(count1))
print()
#print count of the entered number 
'''count1=int(input("enter as any numbers you want i'll give u the  total count:"))
lst1=list(count1)
print(lst1)
print(type(lst1))'''

num=int(input("enter the number whoes length you want to count:"))
count=0
while num > 0:
  num=num//10
  count+=1
print(count)

print()
#print factorial 
fact=int(input("enter the number whoes factorial you want:"))
multi=1
for i in range(fact):
  multi=multi*fact
  fact-=1
print(multi)
print()
#another way 
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
  fact=fact*i
print(fact)
