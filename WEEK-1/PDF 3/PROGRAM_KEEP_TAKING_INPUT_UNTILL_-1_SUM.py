# THIS IS THE PROGRAM THAT TAKES INPUT FROM THE USER UNLESS -1 IS PRESSED AND SUM ALL THE INPUTS
number = 0
sum1 = 0
while number != -1:
   # WE WILL TAKE INPUT UNTILL NUMBER IS EQUAL TO -1
    number = int(input("ENTER A NUMBER ="))
    sum1 = sum1+number

print("THE SUM OF THE VALUES ENTERED ARE =", sum1)
