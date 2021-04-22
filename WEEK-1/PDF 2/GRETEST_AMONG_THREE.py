number1 = float(input("ENTER 1ST NUMBER "))
number2 = float(input("ENTER 2ND NUMBER "))
number3 = float(input("ENTER 3RD NUMBER "))
if(number1 > number2):
    if(number1 > number3):
        print("NUMBER 1 IS THE GRETEST ")
    else:
        print("NUMBER 3 IS THE GRETEST ")

if(number2 > number3):
    if(number2 > number1):
        print("NUMBER 2 IS THE GRETEST ")
    else:
        print("NUMBER 1 IS THE GRETEST ")
