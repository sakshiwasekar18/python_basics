#student result management system

total_marks=500
min_marks=40
max_marks=100

def std_detail():
  '''info=["name", "roll_no"]
  for i in info:
    (f"enter your {i}:")'''
  global name
  global roll_num
  name=input("enter your name: ").strip()
  roll_num=int(input("enter your Roll_no.: "))


def marks():
  sub=["maths","science","chemistry","hindi","english"]
  global obtain_marks
  obtain_marks=0
  for subject in sub:
   marks=int(input(f"enter marks for {subject} :"))
   obtain_marks = obtain_marks + marks

  # print(obtain_marks)

def total_per():
  global percentage
  print(f"total obtained: {obtain_marks}")
  percentage=(obtain_marks/total_marks)*100
  print(f"total percentage: {percentage}%")
# total_per()

def pass_fail():
  if (obtain_marks>=min_marks):
    print("PASS")
  else:
    print("FAIL")

def Garde():
  if  percentage>=90:
    print("garde : A")
  elif 90> percentage>=80:
    print("garde : B")
  elif 80> percentage>=60:
    print("garde : C")
  elif 60> percentage>50:
    print("garde : D")
  else:
    print("garde : F")
  

def format():
  print(f"Student Name:{name}")
  print(f"Student ROLL_NO.:{roll_num}")
  print(f"Total Marks :{obtain_marks}")
  print(f"percentage :{percentage}")
  

def main():
  while True: 
    std_detail()
    marks()
    total_per()
    print()
    format()
    Garde()
    pass_fail()
    print()
    choice=input("you want to enter for another student ,(yes/no):").strip().lower()
    if choice!="yes":
      print("closing student result management system")
      break
main()