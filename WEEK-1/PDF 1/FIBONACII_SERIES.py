# FIBANACi series start from  two numbers and the others terms are obtained by adding the two terms .then making the other term the firs term and the other second continue

# taking first number from the user
first_number = input("ENTER FIRST NUMBER =")

# taking second number from the user
second_number = input("ENTER SECOND NUMBER =")

# converting the numbers into integers
first_number = int(first_number)
second_number = int(second_number)

# calculating fibonacii next term by adding first two terms
fibonaci_series = first_number + second_number

print(fibonaci_series)
# replacing second number to first and new fibanaci term to second
first_number = second_number
second_number = fibonaci_series

fibonaci_series = first_number + second_number
print(fibonaci_series)
first_number = second_number
second_number = fibonaci_series

fibonaci_series = first_number + second_number
print(fibonaci_series)
first_number = second_number
second_number = fibonaci_series

fibonaci_series = first_number + second_number
print(fibonaci_series)
first_number = second_number
second_number = fibonaci_series

fibonaci_series = first_number + second_number
print(fibonaci_series)
