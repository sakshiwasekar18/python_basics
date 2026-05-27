#************************** WRITE IN CSV ***************************
import csv 
# with open(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\file_handling\student.csv","w") as file:
#   write =csv.writer(file)
#   write.writerow(["name","age","marks"])   # this adds line with space 
#   write.writerow(["shanti","43","45"])
#   write.writerow(["shanti","43","45"])

#understanding new line : add line without space 

# with open(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\file_handling\student.csv","w", newline="") as file:   #add line without space 
#   write =csv.writer(file)
#   write.writerow(["name","age","marks"])
#   write.writerow(["shanti","43","45"])
#   write.writerow(["shanti","43","45"])


#************************** APPEND  IN CSV ***************************
# with open(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\file_handling\student.csv","a", newline="") as file:   #add line without space (REPLACED w with a )
#   write =csv.writer(file)
#   write.writerow(["name","age","marks"])
#   write.writerow(["shanti","43","45"])
#   write.writerow(["shanti","43","45"])



#**********************WRITE USING KEY VALUES PAIR *********************
with open(r"C:\Users\91862\Desktop\SAKSHI_PYTHON\file_handling\student.csv","w", newline="") as file:
  fieldnames1=["sr.","age","marks","per"]
  writer= csv.DictWriter(file,fieldnames=fieldnames1)

  writer.writeheader()
  writer.writerow({"sr.":1,"age":20,"marks":89,"per":78})