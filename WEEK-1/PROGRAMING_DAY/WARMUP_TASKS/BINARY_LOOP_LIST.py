# PROGRAM TO CONVERT A NUMBER INTO BINARY
# taking a list to store binary number
binary = []
temp = []
# TAKING ANUMBER AS A INPUT
number = int(input("ENTER A NUMBER ="))
# EXECUTING LOOP UNTILL A NUMBER IS NOT EUAL TO ZERO
while number != 0:
    temp = number % 2
    binary.append(temp)
    number = int(number/2)
binary.reverse()
print(binary)
for i in binary:
    print(i)
