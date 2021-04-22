# PROGRAM TO TEL LWHETHER A NUMBER IS PRIME OR NOT
# TAKIMG A NUMBER AS A INPUT
number = int(input("ENTER A POSITIVE INTEGER ="))
counter = 0
condition = False
# COMPARIG THAT IF NUMBER IS NOT EQUAL TO 2 OR 1 THEN STATEMENTS IN IT WILL BE EXECUTED OTHERWISE NOT
if(number != 2 and number != 1):
    for i in range(2, number+1):
        if(i != number):
            if(number % i == 0):
                counter = counter+1
                # IF THE NUMBER DIVIDED BY ANY NUMBER OTHER THAN ITSELF AND 1 IT WILL NOT BE PRIME
                print("ITS NOT A PRIME NUMBER ")
                break
            else:
                condition = True

else:
    print("ITS A PRIME NUMBER ")
if(condition == True and counter == 0):
    print("ITS A PRIME NUMBER ")
