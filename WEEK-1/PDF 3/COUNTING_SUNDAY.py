day1 = int(input("ENTER DAY ="))
month1 = int(input("ENTER MONTH ="))
year1 = int(input("ENTER YEAR ="))

day2 = int(input("ENTER DAY ="))
month2 = int(input("ENTER MONTH ="))
year2 = int(input("ENTER YEAR ="))

diff = year2-year1
diff = diff*365
days = 0
while day1 != day2 and month1 != month2:

    if(day1 == 31 and (month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12)):
        day1 = 0
        month1 = month1+1

    if(day1 == 30 and (month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11)):
        day1 == 0
        month1 = month1+1
    if(day1 == 29 and month1 == 2):
        day1 = 0
        month1 = month1+1

    day1 = day1+1
    days = days+1

mega_diff = diff-days
mega_diff = mega_diff/7
print("NUMBER OF SUNDAYS BETWEEN TWO DATE ARE =", mega_diff)
