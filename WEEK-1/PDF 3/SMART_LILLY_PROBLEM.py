# SMART LILY PROBLEM
# TAKING AGE AS A INPUT
age = int(input(" ENTER AGE ="))
# TAKING PRICE OF THE WSHING MACHINE AS THE INPUT
pricewm = float(input("ENTER PRICE OF THE WASHING MACHINE ="))
# TAKING TOYPRICES AS THE INPUT
toyprice = float(input("ENTER PRICE OF THE TOY ="))
toys = 0
toys = float(toys)
money = 0
newmoney = 0
# EXECUTING LOOP ACCIRDING TO THE CONDITION
for x in range(1, age+1):
    # APPLYING FORMULAS
    if(x % 2 == 0):

        money = money+10

        newmoney = newmoney+money
        newmoney = newmoney-1

    else:
        toys = toys+1


savedmoney = newmoney+(toys*toyprice)

extramoney = savedmoney-pricewm

# BY COMPARISONS
if(savedmoney >= pricewm):
    print("YES SHE CAN PURCHASED WASHING MACHINE AND HAVE REMAINING ",
          extramoney, " U.S.D")


else:
    print("NO SHE CANNOT PURCHASED WASHING MACHINE  SHE WILL NEED ", -
          extramoney, "  U.S.D SSTO BUY A WASHING MACHINE")
