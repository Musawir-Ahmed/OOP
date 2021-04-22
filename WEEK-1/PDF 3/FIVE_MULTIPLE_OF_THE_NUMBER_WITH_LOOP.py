# PROGRAM TO PRINT MULTIPLE OF THE GIVEN NUMBER
# TAKING NUMBER AS A INPUT
number1 = int(input("ENTER ANY NUMBER ="))
# TO ADD SPACE
print("\n")
# HEADINGS
print("MULTIPLES OF THE NUMBER IS")
# EXECUTING LOOP FROM 1 TO 5
for i in range(1, 6):
    multiple1 = i*number1
    print(number1, " * ", i, " = ", multiple1)
