# PROGRAM TO ADD ALL THE MULTIPLES OF 7 3 8 FROM 0 TO 5000
sum1 = 0
for i in range(0, 5001):
    # COMPARISON  TO FIND MULTIPLES OF THE NUMBER
    if(i % 7 == 0 or i % 3 == 0 or i % 8 == 0):
        sum1 = sum1+i
print("SUM OF THE MULTIPLES OF THE 7 3 8 FROM 0 TO 5000 IS ", sum1)
