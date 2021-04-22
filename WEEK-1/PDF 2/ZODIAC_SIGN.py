# TAKING THE DAY AND THE MONTH FROM THE USER AS THE INPUT
day = int(input("ENTER DAY OF YOUR BIRTH ="))
month = int(input("ENTER MONTH OF YOUR BIRTH ="))
# COMPARING THE DATA ACCORDING TO THE ZODIAC CALEDERS
if((day >= 22 and day <= 31 and month == 12) or (day >= 1 and day <= 20 and month == 1)):
    print("YOUR STAR IS CAPRICON")
elif((day >= 21 and day <= 31 and month == 1) or (day >= 1 and day <= 19 and month == 2)):
    print("YOUR STAR IS AQUARIUS")
elif((day >= 20 and day <= 29 and month == 2) or (day >= 1 and day <= 20 and month == 3)):
    print("YOUR STAR IS PISCES")
elif((day >= 21 and day <= 31 and month == 3) or (day >= 1 and day <= 19 and month == 4)):
    print("YOUR STAR IS ARIES")
elif((day >= 20 and day <= 30 and month == 4) or (day >= 1 and day <= 20 and month == 5)):
    print("YOUR STAR IS TAURUS")
elif((day >= 21 and day <= 31 and month == 5) or (day >= 1 and day <= 21 and month == 6)):
    print("YOUR STAR IS GEMINI")
elif((day >= 22 and day <= 30 and month == 6) or (day >= 1 and day <= 23 and month == 7)):
    print("YOUR STAR IS CANCER")
elif((day >= 24 and day <= 31 and month == 7) or (day >= 1 and day <= 23 and month == 8)):
    print("YOUR STAR IS LEO")
elif((day >= 24 and day <= 31 and month == 8) or (day >= 1 and day <= 22 and month == 9)):
    print("YOUR STAR IS VIRGO")
elif((day >= 23 and day <= 30 and month == 9) or (day >= 1 and day <= 22 and month == 10)):
    print("YOUR STAR IS LIBRA")
elif((day >= 23 and day <= 31 and month == 10) or (day >= 1 and day <= 22 and month == 11)):
    print("YOUR STAR IS SCORPIO")
elif((day >= 23 and day <= 30 and month == 11) or (day >= 1 and day <= 31 and month == 12)):
    print("YOUR STAR IS SAGITARIUS")
