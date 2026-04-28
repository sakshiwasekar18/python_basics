'''
Project Objectives
The system aims to:
1. Accept student details
2. Take marks for multiple subjects
3. Calculate total marks and percentage
4. Determine pass/fail status
5. Assign grades based on performance
6. Handle multiple students in one run
7. Display results in a clean format

Exit the program safely when required
'''

'''
to start debug use 
import pdb; pdb.set_trace()
'''

print("Want to enter student details ?")


# noOfSubjects = 5
# maxMarks = 100
# minMarks = 35
totalMarks = 500


def collectDetails():
        global name
        global roll_no
        name = input("Enter student name: ").strip()
        roll_no = int(input("Enter roll-no: "))
        
def subjectMarksEntry():
    lst = ["Maths: ", "Chemistry: ", "Physics: ", "CS: ", "English: "]
    global obtainMarks
    obtainMarks = 0
    
    for subjects in lst:
        global marks
        marks = int(input(f"Enter marks for {subjects}"))
        if 0 <= marks <= 100:
            obtainMarks += marks
        else:
            break
            
def calculatePercentage():
    global percentage
    percentage = (obtainMarks / totalMarks) * 100
    print(f"Calculate percentage obtain is {percentage}")
    
def PassFail():
    if percentage >= 40:
        return "PASS"
    else:
        return "FAIL"
        
def GradeSystem():
    if percentage >= 90:
        return "A"
    elif 75 <= percentage <= 89:
        return "B"
    elif 60 <= percentage <= 74:
        return "C"
    elif 40 <= percentage <= 59:
        return "D"
    else:
        return "FAIL"
        
def DisplayResult():
    print(f"Student Name: {name}")
    print(f"Roll Number: {roll_no}")
    print(f"Total obatain marks: {obtainMarks}")
    print(f"Percentage obtained: {percentage}")
    print("Result status: " + PassFail())
    print("Grade: " + GradeSystem())
                
    
def main():
    while True:
        collectDetails()
        subjectMarksEntry()
        calculatePercentage()
        DisplayResult()
        
        choice = input("\nWant to add another student? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thank you for using Student Management System.")
            break

if __name__ == "__main__":
    print("Welcome to Student Management System...")
    main()    

            

 
