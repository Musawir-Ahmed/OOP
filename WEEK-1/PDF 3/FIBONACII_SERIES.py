# FIBANACi series start from  two numbers and the others terms are obtained by adding the two terms .then making the other term the firs term and the other second continue

# taking first number from the user
first_number = input("ENTER FIRST NUMBER =")

# taking second number from the user
second_number = input("ENTER SECOND NUMBER =")

# NUMER OF TERMS OF FIBOACII  SERIES
loop_control_variable = input("ENTER NUMBER OF TERMS OF FIBONACCI SERIES =")

# converting the numbers into integers
first_number = int(first_number)
second_number = int(second_number)
loop_control_variable = int(loop_control_variable)
print(first_number)
print(second_number)
# calculating fibonacii next term by adding first two terms
for i in range(0, loop_control_variable-2):
    fibonaci_series = first_number + second_number
    print(fibonaci_series)
# replacing second number to first and new fibanaci term to second
    first_number = second_number
    second_number = fibonaci_series
