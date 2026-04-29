print()
#grade for marks and avg
print("grade for marks")
a=int(input("enter the marks for maths :"))
b=int(input("enter the marks for english:"))
c=int(input("enter the marks for hindi :"))
d=int(input("enter the marks for science :"))
e=int(input("enter the marks for social science :"))
print()
total_mark=500
total=a+b+c+d+e
print(f" total: {total}")
percentage= (total/total_mark)*100
print(f"percentage : {percentage}%")

avg=a+b+c+d+e/5
print(f"avgerage : {avg}")

#by short hand if 
print("grade :A") if percentage>=90 else print("garde : B") if percentage< 90 and percentage>=80 else print("grade :C") if percentage<80 and percentage>=70 else print("grade :D") if percentage<70 and percentage>=45 else print("FAIL")


print()
#greater or equale
a=int(input("enter a number:" ))
b=int(input("enter a number:" ))

print("a is greater") if a>b else print("b is greater") if b>a else print("both are equal")