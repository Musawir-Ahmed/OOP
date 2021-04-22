# TAKING MARKS OF THR USER AS THE INPUT
marks = int(input(" ENTER YOUR MARKS OUT OF 100 ="))

if(marks < 0 or marks > 100):
    print("INVALID MARKS")
else:
    # CAMPARING BY  THE GIVEN SCHEME
    if(marks <= 25):
        print("YOUR GRADE IS F")
    if(marks >= 26 and marks <= 45):
        print("YOUR GRADE IS E")
    if(marks >= 46 and marks <= 50):
        print("YOUR GRADE IS D")
    if(marks >= 51 and marks <= 60):
        print("YOUR GRADE IS C")
    if(marks >= 61 and marks <= 80):
        print("YOUR GRADE IS B")
    if(marks > 80):
        print("YOUR GRADE IS A")
