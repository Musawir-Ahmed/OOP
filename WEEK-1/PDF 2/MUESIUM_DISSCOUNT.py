# TAKING DAY NUMBER FROM THE USER AS A INPUT
day_number = int(input("ENTER DAY IN NUMBER ="))
# TAKING AGE FROM THE USER AS THE INPUT
age = int(input("ENTER YOUR AGE ="))
# COMPARING AS THE GIVEN CONDITIONS
if(day_number == 1):
    print("MUESIUM IS CLOSED ON MONDAY")
elif(day_number == 2 or day_number == 4):
    print("YOU GOT HALF PRICE DISSCOUNT")
elif(age >= 13 and age <= 20):
    print("YOU GOT DISSCOUNT ON WEDNESDAY")
elif(age < 6 and age > 65):
    print("YOU ADMISSION IS FREE")
elif(age >= 6 and age <= 12):
    print("YOU ADMISSION IS HALF PRICED ON WEEKENDS")
else:
    print("YOU DIDNT GET ANY DISSCOUNT")
