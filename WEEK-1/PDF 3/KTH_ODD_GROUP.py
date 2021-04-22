# PROGRAM TO FIND THE Sum of Kth Odd Group
# TAKING A NUMBER AS A INPUT
number = int(input("ENTER VALUE OF K ="))
count = 0
sum1 = 0
# FORMULA TO FIND THE K TERM
k_value = (number*number)-number+1
# EXECUTING LOOP ACCORDING TO THE K_VALUE AND INCREASING IT BY 2
for i in range(k_value, 101, 2):
    count = count+1
    sum1 = sum1+i
    if(count == number):
        break
print("SUM OF THE Kth ODD GROUP IS =", sum1)
