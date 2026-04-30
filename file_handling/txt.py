import traceback


# file=open("demo.txt","x")
# file=open(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\file_handling\demo2.txt","x")
#read operations
'''file=open("demo.txt","r")
print(file.readable()) #retuens if file can be read or not ,returns boolean
print(file.readline()) #reads 1st line of a file

print(file.readlines()) # returns data in list also recognises\n
print(file.read())  # reads all text , all lines in file 

#best practice
# with open("demo.txt","r")as file :
  # print(file.read())

#execption handling(error handling) with file handling
try:
  with open("demoy.txt","r")as file:
    print(file.read())
except FileNotFoundError:
  print(" \n spelling mistake or mode error")
  traceback.print_exc()


#write operations

file=open("demo2.txt","w") 
print(file.writable())
file.writelines(["hi ia m human","\nhumans are kind"])
file.write("hello \n hi")
# with open("demo2.txt","w") as file:
#  print( file.writable())

#exception handling with write

try:
  with open("demo2.txt","w") as f: #it creats a file and updates the data so no error 
    f.write("hello madam hjj helo")
except FileExistsError:
  print("file name error or mode aeeror")
  traceback.print_exc()'''


#append : only in write , only 2 operations as write() and writelines()

with open("demo.txt","a") as file:
  print(file.readable())
  print(file.writable())
  file.write("how are you \n doing")
  file.writelines(["\n i am fine","\n thank you"])



