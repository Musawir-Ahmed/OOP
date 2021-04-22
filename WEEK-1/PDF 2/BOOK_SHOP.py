# TAKING NUMBER OF BOOKS FROM THE USER AS INPUT
number_of_books = int(input("ENTER NUMBER OF BOOKS YOU PURCHASED ="))
# CALCULATING PRICE OF THE BOOK
total_price = number_of_books*100
# BY COMPARING CONDITIONS
if(total_price > 1000):
    disscount = total_price*0.1
    total_price = total_price-disscount
print(" PAYABLE AMMOUNT IS =", total_price)
