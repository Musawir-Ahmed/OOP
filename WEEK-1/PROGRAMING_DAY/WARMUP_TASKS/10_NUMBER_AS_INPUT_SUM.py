# making a list to input data
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum1 = 0
for i in range(0, 10):
    temp = int(input("ENTER A NUMBER ="))
    sum1 = sum1+temp
    number[i] = temp
print(number)
print("SUM OF THE NUMBERS ARE =", sum1)
