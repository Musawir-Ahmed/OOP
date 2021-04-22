# MAKING A LIST TO STORE
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum1 = 0
# taking input from the user in the list
for i in range(0, 10):
    number[i] = int(input("ENTER A NUMBER ="))
print(number)
# USING LOOP TO SUM ALL THE ELEMENTS IN  A LIST
for i in range(0, 10):
    sum1 = sum1+number[i]
print("SUM OF THE NUMBERS IN AN LIST ARE ", sum1)
