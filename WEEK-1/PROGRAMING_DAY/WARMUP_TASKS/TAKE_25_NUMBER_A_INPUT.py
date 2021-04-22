# TAKING A LIST TO STORE NUMBER ENTERED BY THE USER
number = []
new_list = []
for i in range(0, 25):
    number.append(int(input("ENTER A NUMBER = ")))
# APPLYING LOOP TO EXTRACT NUMBERS THAT ARE ODD AND DIVISIBLE BY 5
for i in number:
    if(i % 2 != 0 and i % 5 == 0):
        new_list.append(i)
print(new_list)
