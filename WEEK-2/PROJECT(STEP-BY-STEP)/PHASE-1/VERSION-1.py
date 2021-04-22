print("**************************************************************************************************\n")
print("                                      BANK MANAGEMENT SYSTEM                                      \n")
print("**************************************************************************************************\n")
print("---------------------------------------------------------------------------------------------------\n")
# to calculate profit on the ammount deposited in the acoount according to the year in which it is deposited
year = int(input("ENTER YEAR IN WHICH YOU DEPOSITED AMMOUNT="))
ammount = int(input("ENTER AMMOUNT DEPOSITED ="))
# on every year 1% profit is generated on the deposited ammount
profit_percentage = 0
profit_percentage = year/100
profit = ammount*profit_percentage
print("YOU HAVE GOT THE PROFIT OF RS =", profit)
profit = ammount+profit
print("NOW YOUR AMMOUNT IN YOUR ACCOUNT IS=", profit)
