# TAKING A LIST TO STORE NUMBER ENTERED BY THE USER
number = []
new_list = []
sum1 = 0
for i in range(0, 20):
    number.append(int(input("ENTER A NUMBER = ")))
# APPLYING LOOP TO EXTRACT NUMBERS THAT ARE ODD AND DIVISIBLE BY 5
for i in number:
    sum1 = sum1+i
print("SUM OF THE NUMBERS ARE ", sum1)
