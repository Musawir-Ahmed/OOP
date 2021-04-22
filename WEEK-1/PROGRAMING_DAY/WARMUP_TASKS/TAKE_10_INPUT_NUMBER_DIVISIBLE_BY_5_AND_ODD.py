# MAKING A LIST TO STORE
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
new_list = []
count = 0
# taking input from the user in the list
for i in range(0, 10):
    number[i] = int(input("ENTER A NUMBER ="))
print(number)
# NOW APPLYING LOOP TO EXTRACT NUMBER THAT ARE ODD AND DIVISIBLE BY 5
for i in range(0, 10):
    temp = number[i]
    if (temp % 2 != 0 and temp % 5 == 0):
        new_list.append(temp)
print(new_list)
