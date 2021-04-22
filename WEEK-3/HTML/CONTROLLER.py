# importing flask
from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")


class Student:
    email = ""
    password = ""
    username = ""
    record = []
    gpa = "0"


student = Student()

# THIS ROUTE TRANSFERS CONTROL TO SIGNN PAGE


@ app.route("/")
def signin():
    return render_template("SIGNIN.html")

# THIS ROUT TRANSFER CONTROL TO SIGNUP PAGE


@ app.route("/SIGNUP.html")
def signup():
    return render_template("SIGNUP.html")

# THIS ROUT GIVES US THE DATA THAT IS INPUTED IN THE FORMS IN SIGNUP


@app.route("/signupdata", methods=['POST', 'GET'])
def data_signup():
    student.email = request.form['email']
    student.username = request.form['username']
    student.password = request.form['password']
    sign_up(student)
    return signin()

# THIS FUNCTION STORED THE DATA INPUTED IN THE FORM TO A FILE


def sign_up(student):
    gpa = str(0)
    myfile = open("SIGN.txt", "a")
    record = student.email+","+student.username + \
        ","+student.password+","+student.gpa+","
    print(record, file=myfile, sep="\n")
    myfile.close()
    print(" RECORD HAS BEEN ADDED SUESSFULLY .......................")

# THIS FUNCTION EXTRACT THE ATTRIBUTES THAT ARE STORED IN A FILE BY COMMAS


def get_field(field, commano):
    commano = int(commano)
    comma_counter = 0
    counter = 0
    diff = commano-1
    temp = ""

    while comma_counter < commano:

        if comma_counter >= diff and comma_counter < commano:
            temp = temp+field[counter]

        if(field[counter+1] == ","):
            comma_counter = comma_counter+1
            counter = counter+1

        counter = counter+1

    return temp

# THIS FUNCTION RETURNS A CONDITION THAT A THE USER EXITS OR NOT IF IT EXITS IT RENDER IT TO THE MAIN PAGE IF NOT IT RETURNS FALSE


def sign_in(student):
    global gpa
    myfile = open("SIGN.txt", "r")
    record = myfile.read().splitlines()
    myfile.close
    condition = True
    for field in record:
        temp_email = get_field(field, 1)
        tem_password = get_field(field, 3)

        print(tem_password, temp_email)
        if(temp_email == student.email and tem_password == student.password):
            gpa = get_field(field, 4)
            day = []
            teachername = []
            time = []
            subject = []
            return render_template("TIMETABLE.html", day=day, teachername=teachername, time=time, subject=subject, len=len(day))
        else:
            condition = False
    if condition == False:
        return render_template("SIGNIN.html")

# THIS ROUT GIVES US THE DATA THAT IS INPUTED IN THE SIGN IN FORMS


@app.route("/signindata", methods=['POST', 'GET'])
def data_signin():

    student.email = request.form['email']
    student.password = request.form['password']
    condition = sign_in(student)
    return condition

# THIS ROUT TRANSFERS THE CONTROL TO THE TIMETABLE PAGE


@ app.route("/TIMETABLE")
def timetable():
    day = []
    teachername = []
    time = []
    subject = []
    return render_template("TIMETABLE.html", day=day, teachername=teachername, time=time, subject=subject, len=len(day))

# THIS CLASS IS USED TO STORE THE TIME TABLE DATA OF THE STUDENT INTO THE FILE


class Studentrecord:
    day = ""
    teachername = ""
    time = ""
    subject = ""

# THIS FUNCTION WRITE THE TIME TABLE DATA INTO THE FILE


def write_time_table_data(temp):
    myfile = open("TIMETABLE.txt", "a")
    print(temp, file=myfile, sep="\n")
    myfile.close()

# THIS ROUT GIVES US THE DATA INPUTED IN THE TINETABLE FORMS


@app.route("/data", methods=['POST', 'GET'])
def data_timetable():
    studentdata = Studentrecord()
    studentdata.day = request.form['day']
    studentdata.teachername = request.form['teachername']
    studentdata.time = request.form['time']
    studentdata.subject = request.form['subject']
    temp = student.email+","+student.password+","+studentdata.day+"," + \
        studentdata.teachername+","+studentdata.time+","+studentdata.subject+","
    print(temp)
    write_time_table_data(temp)
    day = []
    teachername = []
    time = []
    subject = []
    return render_template("TIMETABLE.html", day=day, teachername=teachername, time=time, subject=subject, len=len(day))

# THIS FUNTION READS THE DATA OF THE USER LOGED IN AND TRANSFER THAT DATA IN TO THE RELOAD ROUT IN THE FORM OF THE LIST


def read_time_table_data():
    myfile = open("TIMETABLE.txt", "r")
    record = myfile.read().splitlines()
    myfile.close
    print(record)
    return record

# THIS ROUTE READS THE DATA OF THE USER THAT IS LOGED IN AND SEPERATE IT AND STORED IT INTO DIFFRENT ARRAYS OF DAYS TEACHERNAME TIME SUBJECT AND GIVED THESE ARRAY AND THERE LENGTH TO THE TIME TABLE WEB PAGE


@ app.route("/RELOAD:TIME:TABLE")
def reloadtimetable():
    record = read_time_table_data()
    day = []
    teachername = []
    time = []
    subject = []
    for field in record:
        temp_email = get_field(field, 1)
        tem_password = get_field(field, 2)
        if(student.email == temp_email and student.password == tem_password):
            temp_day = get_field(field, 3)
            temp_teachername = get_field(field, 4)
            temp_time = get_field(field, 5)
            temp_subject = get_field(field, 6)
            day.append(temp_day)
            teachername.append(temp_teachername)
            time.append(temp_time)
            subject.append(temp_subject)
    print("list", day, teachername, time, subject)
    return render_template("TIMETABLE.html", day=day, teachername=teachername, time=time, subject=subject, len=len(day))


# THIS ROUT TRANSFERS CONTROL TO THE GPA CALCULATOR PAGE
@ app.route("/GPACALCULATOR")
def gpacalculator():
    result = 0
    return render_template("GPACALCULATOR.HTML", result=result)

# CLASS THAT IS USED TO STORE THE DATA THAT IS INPUTTED IN THE FORM IN GPA CALCULATOR PAGE


class Gpadata:
    credit = ""
    grade = 1
    total = 1

# THIS FUNCTION TAKES THE CREDIT HOURS AND GRADE OF THE STUDENT AND CALCULATES ITS CREDIT POINTS


def credithour(credit, grade):
    credit = float(credit)
    calculate = int(0)

    if grade == "A+":
        grade = 4
    elif grade == "A":
        grade = 4
    elif grade == "A-":
        grade = 3.7
    elif grade == "B+":
        grade = 3.3
    elif grade == "B":
        grade = 3
    elif grade == "B-":
        grade = 2.6
    elif grade == "C+":
        grade = 2.3
    elif grade == "C":
        grade = 2
    elif grade == "C-":
        grade = 1.6
    elif grade == "D+":
        grade = 1.3
    elif grade == "F":
        grade = 0
        credit = 1

    calculate = credit*grade
    print(credit, calculate)
    return calculate


'''
THIS ROUT GETS THE DATA THAT IS ENTERED IN THE FORM IN GPA CALULATOR AND CALCULATES THE GPA OF THE 
STUDENT IF ANY OF THE FIELS IS EMPTY IS JUST IGNORS THEM AND CALCULATES THE STUDEBT GPA
'''


@app.route("/gpadata", methods=['POST', 'GET'])
def data_gpa():
    add = 0
    add_credit_hours = float(0)
    gpa1 = Gpadata()
    gpa1.credit = request.form['credithour1']
    gpa1.grade = request.form['grade1']
    print(gpa1.credit, gpa1.grade)
    if gpa1.grade != "":
        gpa1.credit = float(gpa1.credit)
        gpa1.total = credithour(gpa1.credit, gpa1.grade)
        add = add+gpa1.total
        add_credit_hours = add_credit_hours+gpa1.credit
    print("GPA =", gpa1.total)
    print("ADD", add, "CREDIT HOUR", add_credit_hours)

    gpa2 = Gpadata()
    gpa2.credit = request.form['credithour2']
    gpa2.grade = request.form['grade2']
    print(gpa2.credit, gpa2.grade)
    if gpa2.grade != "":
        gpa2.credit = float(gpa2.credit)
        gpa2.total = credithour(gpa2.credit, gpa2.grade)
        add = add+gpa2.total
        add_credit_hours = add_credit_hours+gpa2.credit

    gpa3 = Gpadata()
    gpa3.credit = request.form['credithour3']
    gpa3.grade = request.form['grade3']
    print(gpa3.credit, gpa3.grade)
    if gpa3.grade != "":
        gpa3.credit = float(gpa3.credit)
        gpa3.total = credithour(gpa3.credit, gpa3.grade)
        add = add+gpa3.total
        add_credit_hours = add_credit_hours+gpa3.credit

    gpa4 = Gpadata()
    gpa4.credit = request.form['credithour4']
    gpa4.grade = request.form['grade4']
    print(gpa4.credit, gpa4.grade)
    if gpa4.grade != "":
        gpa4.credit = float(gpa4.credit)
        gpa4.total = credithour(gpa4.credit, gpa4.grade)
        add = add+gpa4.total
        add_credit_hours = add_credit_hours+gpa4.credit

    gpa5 = Gpadata()
    gpa5.credit = request.form['credithour5']
    gpa5.grade = request.form['grade5']
    print(gpa5.credit, gpa5.grade)
    if gpa5.grade != "":
        gpa5.credit = float(gpa5.credit)
        gpa5.total = credithour(gpa5.credit, gpa5.grade)
        add = add+gpa5.total
        add_credit_hours = add_credit_hours+gpa5.credit
    result = add/add_credit_hours
    print("RESULT =", result)
    print(add)

    return render_template("GPACALCULATOR.HTML", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
