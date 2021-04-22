# TAKING NUMBER OF WHITE FLOWERS AS A INPUT FROM THE ISER
white_roses = float(input("ENTER NUMBER OF WHITE ROSES YOU WANT TO PRCHASE ="))
# TAKING NUMBER OF RED FLOWERS AS A INPUT FROM THE ISER
red_roses = float(input("ENTER NUMBER OF RED ROSES YOU WANT TO PRCHASE ="))
# TAKING NUMBER OF TULIPS FLOWERS AS A INPUT FROM THE ISER
tulips = float(input("ENTER NUMBER OF TULIPS YOU WANT TO PRCHASE ="))
# TAKING SEASON AS THE INPUT
season = input("ENTER SEASON NAME =")
# TAKING Y FOR YES AND N FOR NO TO GET ANSWER FROM THE USER THAT IT IS A WEEKEND OR NOT
holiday = input("ENTER Y IF IT IS HOLIDAY N IS ITS NOT =")
# CALCULATING TOTAL NUMBER OF FLOWERS
total_number = white_roses + red_roses + tulips
# DOING CAMPARISONS ACCORDING TO THE GIVEN CONDITION
if(season == "SPRING" or season == "SUMMER"):
    red_roses_price = red_roses * 2.00
    print(red_roses_price)
    white_roses_price = white_roses * 4.10
    print(white_roses_price)
    tulips_price = tulips * 2.50
    print(tulips_price)

elif(season == "AUTUMN" or season == "WINTER"):
    red_roses_price = red_roses * 3.75
    white_roses_price = white_roses * 4.50
    tulips_price = tulips * 4.15

total_price = red_roses_price + white_roses_price + tulips_price

if(holiday == "Y"):
    increased_price = 0.15 * total_price
    total_price = total_price+increased_price

if(season == "SPRING" and tulips > 7):
    disscount_price = 0.05 * total_price
    total_price = total_price-disscount_price

if(season == "WINTER" and white_roses >= 10):
    disscount_price = 0.1 * total_price
    total_price = total_price-disscount_price

if(total_number > 20):
    disscount_price = 0.2 * total_price
    total_price = total_price-disscount_price

total_price = total_price + 2

print("YOU HAVE TO PAY RS ", total_price, " AFTER DISSCOUNT")
