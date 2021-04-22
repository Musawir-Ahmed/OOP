# TAKING NUMBERS FROM THE USER AS THE INPUT
number1 = int(input("ENTER 1ST NUMBER ="))
number2 = int(input("ENTER 2ND NUMBER ="))
number3 = int(input("ENTER 3RD NUMBER ="))
# COMPARING THE NUMBERS
if((number1 > number2) and (number1 > number3)):
    print("NUMBER 1 IS GRETER AMONG THREE")
if((number2 > number1) and (number2 > number3)):
    print("NUMBER 2 IS GRETER AMONG THREE")
if((number3 > number1) and (number3 > number2)):
    print("NUMBER 3 IS GRETER AMONG THREE")
