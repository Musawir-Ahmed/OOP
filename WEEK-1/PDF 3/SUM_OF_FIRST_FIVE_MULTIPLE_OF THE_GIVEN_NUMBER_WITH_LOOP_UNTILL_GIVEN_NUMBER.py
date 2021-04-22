# PROGRAM TO SUM THE MULTIPLES OF THW TWO NUMBER YNTIL THE GIVEN NUMBER
number1 = int(input("ENTER ANY 1ST NUMBER ="))
number2 = int(input("ENTER ANY 2ND NUMBER ="))
total_no = int(input("ENTER NUMBER OF MULTIPLE ="))
sum = 0
# TO ADD SPACE
print("\n")
# HEADINGS
print("MULTIPLES OF THE FIRST NUMBER IS", "\t \t",
      "MULTIPLES OF THE SECOND NUMBER IS")

for i in range(1, total_no+1):
    multiple1 = i*number1
    multiple2 = i*number2
    print(number1, " * ", i, " = ", multiple1,
          "\t \t \t \t \t", number2, " * ", i, " = ", multiple2)
    sum = sum+multiple1+multiple2


print("\n SUM OF THE MULTIPLES OF THE TWO NUMBERS IS =", sum)
