number1 = int(input("ENTER ANY 1ST NUMBER ="))
number2 = int(input("ENTER ANY 2ND NUMBER ="))

print("\n")

print("MULTIPLES OF THE FIRST NUMBER IS", "\t \t",
      "MULTIPLES OF THE SECOND NUMBER IS")

for i in range(1, 6):
    multiple1 = i*number1
    multiple2 = i*number2
    print(number1, " * ", i, " = ", multiple1,
          "\t \t \t \t \t", number2, " * ", i, " = ", multiple2)
