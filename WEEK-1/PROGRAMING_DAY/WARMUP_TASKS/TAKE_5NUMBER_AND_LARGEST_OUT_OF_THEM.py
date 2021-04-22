# making a list to input data
number = [0, 0, 0, 0, 0]
largest = -10000
for i in range(0, 5):
    temp = int(input("ENTER A NUMBER ="))
    if(largest < temp):
        largest = temp
    number[i] = temp
print(number)
print("LARGEST NUMBER IN THE LIST IS =", largest)
