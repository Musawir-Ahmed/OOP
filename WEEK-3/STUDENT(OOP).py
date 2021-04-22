import os


class studentinfo:
    sname = ""
    rollno = 0
    gpa = 0.0
    isHostelide = ""
    Department = ""


def header():
    print("**************************************************************************\n")
    print("                                STUDENT RECORD                            \n")
    print("**************************************************************************\n")
    print("--------------------------------------------------------------------------\n")


def displayoptions():
    print("1.ADD STUDEN")
    print("2.SHOW STUDENT")
    print("3.LIST TOP STUDENT")
    print("4.EXIT")


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def presskey():
    input("PRESS ENTER TO CONTINUE.............")


def displaystudentinfo(s1, s2, s3):
    print("NAME\tROLL NO\tGPA\tHOSTELIDE\tDEPARTMENT")
    if(s1.sname != ""):
        if(s1.sname != ""):
            print(s1.sname, "\t", s1.rollno, "\t", s1.gpa,
                  "\t", s1.isHostelide, "\t", s1.Department)
    if(s2.sname != ""):
        if(s2.sname != ""):
            print(s2.sname, "\t", s2.rollno, "\t", s2.gpa,
                  "\t", s2.isHostelide, "\t", s2.Department)
    if(s3.sname != ""):
        if(s3.sname != ""):
            print(s3.sname, "\t", s3.rollno, "\t", s3.gpa,
                  "\t", s3.isHostelide, "\t", s3.Department)


def topstudent(s1, s2, s3):
    print("NAME\tROLL NO\tGPA\tHOSTELIDE\tDEPARTMENT")

    s1.gpa = float(s1.gpa)
    s2.gpa = float(s2.gpa)
    s3.gpa = float(s3.gpa)

    if (s1.gpa > s2.gpa and s1.gpa > s3.gpa):
        print(s1.sname, "\t", s1.rollno, "\t", s1.gpa,
              "\t", s1.isHostelide, "\t", s1.Department)

    if (s2.gpa > s1.gpa and s2.gpa > s3.gpa):
        print(s2.sname, "\t", s2.rollno, "\t", s2.gpa,
              "\t", s2.isHostelide, "\t", s2.Department)

    if (s3.gpa > s1.gpa and s3.gpa > s2.gpa):
        print(s3.sname, "\t", s3.rollno, "\t", s3.gpa,
              "\t", s3.isHostelide, "\t", s3.Department)


s1 = studentinfo()
s2 = studentinfo()
s3 = studentinfo()

counter = 0
program_running = True
while program_running == True:
    clearscreen()
    header()
    displayoptions()
    option = int(input("ENTER ANY OPTION ="))
    if(option == 1):
        clearscreen()
        header()
        if(counter == 0):
            s1.sname = input("ENTER YOUR NAME =")
            s1.rollno = int(input("ENTER YOUR ROLL NO ="))
            s1.gpa = input("ENTER YOUR GPA =")
            s1.isHostelide = input(
                "ENTER Y IF YOU ARE HOSTALIIED N IF YOU ARE NOT A HOSTALLIED =")
            s1.Department = input("ENTER YOUR DEPARTMENT NAME WITHOUT SPACE =")
        if(counter == 1):
            s2.sname = input("ENTER YOUR NAME =")
            s2.rollno = int(input("ENTER YOUR ROLL NO ="))
            s2.gpa = input("ENTER YOUR GPA =")
            s2.isHostelide = input(
                "ENTER Y IF YOU ARE HOSTALIIED N IF YOU ARE NOT A HOSTALLIED =")
            s2.Department = input("ENTER YOUR DEPARTMENT NAME WITHOUT SPACE =")
        if(counter == 2):
            s3.sname = input("ENTER YOUR NAME =")
            s3.rollno = int(input("ENTER YOUR ROLL NO ="))
            s3.gpa = input("ENTER YOUR GPA =")
            s3.isHostelide = input(
                "ENTER Y IF YOU ARE HOSTALIIED N IF YOU ARE NOT A HOSTALLIED =")
            s3.Department = input("ENTER YOUR DEPARTMENT NAME WITHOUT SPACE =")
            counter = 0
        presskey()
        counter = counter+1

    if(option == 2):
        clearscreen()
        header()
        displaystudentinfo(s1, s2, s3)
        presskey()

    if(option == 3):
        clearscreen()
        header()
        topstudent(s1, s2, s3)
        presskey()
    if(option == 4):
        program_running = False
