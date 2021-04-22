# BACK TO THE PAST PROBLEM
year = 0
inher = 0
age = 18
a = 0
# TAKING YEAR AS THE INPUT
year = int(input("ENTER YEAR="))
# TAKING INHERITANCE AS INPUT
inher = int(input("ENTER INHERITANCE yearOU RECIEVED="))
a = inher
x = 1800
# EXECUTING LOOP UNTIL THE PRESENT YEAR
while x <= year:
    if(x % 2 == 0):
        a = a-12000

    else:
        a = a-(12000+50*(age))

    age = age+1
    x = x+1
# MAKING COMPARISION A WAS EQUAL TO THE INHERITANCE GIVEN IN THE BEGINNING THAT PROCESSED ACCORDING TO THE FORMULA
if(a >= 1):
    print("YES He WILL LIVE CARELESS LIFE")
    print("HE WILL HAVE RS=", a, " LEFT")
if(a < 1):
    print("NO HE CA NOT LIVE A CARELESS LIFE=")
    print("HE WILL NEED RS  = ", -a)
