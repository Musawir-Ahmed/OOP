# to find the first 5 multiple of the number we will multiply them by 1 2 3 4 5

# taking first number from the user
number1 = input("ENTER FIRST NUMBER TO FIND ITS FIVE MULTIPLE =")
number1 = int(number1)

# taking second number from the user
number2 = input("ENTER SECOND NUMBER TO FIND ITS FIVE MULTIPLE =")
number2 = int(number2)

# to find the ultiple of the fiest number
print("MULTIPLES OF THE NUMBER ", number1, " ARE ")
multiple = number1 * 1
sum1 = multiple
print(multiple)
multiple = number1 * 2
sum1 = sum1+multiple
print(multiple)
multiple = number1 * 3
sum1 = sum1+multiple
print(multiple)
multiple = number1 * 4
sum1 = sum1+multiple
print(multiple)
multiple = number1 * 5
sum1 = sum1+multiple
print(multiple)

# to find the ultiple of the second number
print("MULTIPLES OF THE NUMBER ", number2, " ARE ")
multiple = number2 * 1
sum1 = sum1+multiple
print(multiple)
multiple = number2 * 2
sum1 = sum1+multiple
print(multiple)
multiple = number2 * 3
sum1 = sum1+multiple
print(multiple)
multiple = number2 * 4
sum1 = sum1+multiple
print(multiple)
multiple = number2 * 5
sum1 = sum1+multiple
print(multiple)

# to print the sum1 of the multiples of the two numbers
print("SUM OF FIRST FIVE MULTIPLE OF THE GIVEN NUMBER IS =", sum1)
