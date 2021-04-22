# TAKING A LIST TO STORE NUMBER ENTERED BY THE USER
number = []
new_list = []
sum1 = 0
largest = -1000
for i in range(0, 20):
    number.append(int(input("ENTER A NUMBER = ")))
# APPLYING LOOP TO EXTRACT NUMBERS THAT ARE ODD AND DIVISIBLE BY 5
for i in number:
    if(largest < i):
        largest = i
print("LARGEST NUMBER AMONG THE LIST IS  ", largest)
