# THIS PROGRAM CALCULATES FICTORIAL OF THE NUMBER
# TAKING A NUMBER AS A INPUT TO FIND ITS FICTORIAL
loop_control_variable = int(input("ENTER ANY NUMBER ="))
# INITIALIZING IT SO THAT IT CAN E FREE FROM GARBAGE VALUE
fictorial = 1
# EXECUTING LOOP UNTILL THE GIVEN NUMBER
for i in range(1, loop_control_variable+1):
    fictorial = fictorial*i
print("FICTORIAL OF THE NUMBER ", loop_control_variable, " IS", fictorial)
