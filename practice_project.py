# def welcome():
#   print("welcone to student mangement system")
# welcome()
# def show_name(name):
#   print("student name:",name)


# show_name("sakshi")
# show_name("isha")

# def show_name(name,age):
#   print("student name:",name)
#   print("student age:",age)


# show_name("sakshi",20)
# show_name("isha",45)


# def total(mark1,mark2):
#   score=mark1+mark2
#   return score
# result=total(30,80)
# print("result:",result)

#if else in fuction 
# def result(marks):
#   if marks>70:
#     print("pass")
#   else:
#     print("fail")
# result(0)
# result(90)

# student=[]
# def add_stud(name):
#   student.append(name)
#   print("student added",name)
# add_stud("ali")
# add_stud("aliyana")
# add_stud("alina")


student=["ali","nil","savita"]
def check(name):
  if name in student:
    print("student found")
  else:
    print("student not found")
check("sami")
check("savita")