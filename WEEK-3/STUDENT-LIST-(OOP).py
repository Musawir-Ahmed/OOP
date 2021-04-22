
import os

# DECLARING A LIST TO STORE PRODUCT DATA
studentrecord = []

# MADE A CLASS TO STORE STUDENT DATA


class studentinfo:
    sname = ""
    rollno = 0
    gpa = 0.0
    isHostelide = ""
    Department = ""

# DISPLAYING HEADER


def header():
    print("**************************************************************************\n")
    print("                                STUDENT RECORD                            \n")
    print("**************************************************************************\n")
    print("--------------------------------------------------------------------------\n")

# DISPLAYING OPTIONS FUNCTIONS


def displayoptions():
    print("1.ADD STUDEN")
    print("2.SHOW STUDENT")
    print("3.LIST TOP STUDENT")
    print("4.EXIT")

# CLEARING SCREEN


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# PRESS KEY TO  CONTINUE FUNCTION
def presskey():
    input("PRESS ENTER TO CONTINUE.............")


# FUNCTION TO ADD STUDENT
def addstudent(studentrecord):
    student = studentinfo()
    student.sname = input("ENTER YOUR NAME =")
    student.rollno = int(input("ENTER YOUR ROLL NO ="))
    student.gpa = input("ENTER YOUR GPA =")
    student.isHostelide = input(
        "ENTER Y IF YOU ARE HOSTALIIED N IF YOU ARE NOT A HOSTALLIED =")
    student.Department = input("ENTER YOUR DEPARTMENT NAME WITHOUT SPACE =")
    return student


# FUNCTION TO DISPLAY STUDENT RECORD STORED
def displaystudentinfo(studentrecord):
    print("NAME\tROLL NO\tGPA\tHOSTELIDE\tDEPARTMENT")
    for field in studentrecord:
        print(field.sname, "\t", field.rollno, "\t", field.gpa,
              "\t", field.isHostelide, "\t", field.Department, "\n")


# TO SEE THE TOP STUDENT
def topstudent(studentrecord):
    print("NAME\tROLL NO\tGPA\tHOSTELIDE\tDEPARTMENT")
    largest = -10000
    largestidx = 0
    counter = 0
    for field in studentrecord:
        if(largestidx < float(field.gpa)):
            largest = float(field.gpa)
            largestidx = counter
        counter = counter+1

    print(studentrecord[largestidx].sname, "\t", studentrecord[largestidx].rollno, "\t", studentrecord[largestidx].gpa,
          "\t", studentrecord[largestidx].isHostelide, "\t", studentrecord[largestidx].Department)


# MAIN LOOP
counter = 0
program_running = True
while program_running == True:
    clearscreen()
    header()
    displayoptions()
    option = int(input("ENTER ANY OPTION ="))
    if(option == 1):
        clearscreen()
        record = addstudent(studentrecord)
        studentrecord.append(record)
        header()

    if(option == 2):
        clearscreen()
        header()
        displaystudentinfo(studentrecord)
        presskey()

    if(option == 3):
        clearscreen()
        header()
        topstudent(studentrecord)
        presskey()
    if(option == 4):
        program_running = False
