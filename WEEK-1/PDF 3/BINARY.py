# PROGRAM TO CONVERT A NUMBER INTO BINARY
# TAKING ANUMBER AS A INPUT
number = int(input("ENTER A NUMBER ="))
# EXECUTING LOOP UNTILL A NUMBER IS NOT EUAL TO ZERO
while number != 0:
    binary = number % 2
    number = int(number/2)
    print(binary)
