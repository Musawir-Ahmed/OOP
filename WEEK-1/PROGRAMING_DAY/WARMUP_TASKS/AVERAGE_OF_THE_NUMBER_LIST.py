# MAKING LIST TO STORE NUMBER ENTERED BY THE USER
number = []
sum1 = 0
# ASKING HOW MANY NUMBER TEHEY WANT TO ENTER
total_number = int(input("ENTER TOTAL NUMBER OF ELEMENT IN A LIST ="))
for i in range(0, total_number):
    temp = float(input("ENTER A NUMBER ="))
    number.append(temp)
    sum1 = sum1+temp
average = sum1/temp
print("AVERAGE OF THE LIST IS ", average)
