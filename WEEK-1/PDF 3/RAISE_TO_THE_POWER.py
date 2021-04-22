# PROGRAM TO RAISE A NUMBER TO A SPECIFIC POWER
# TAKING A NUMBER AS A INPUT
number = int(input("ENTER A NUMBER ="))
# TAKING ITS POWER AS THE INPUT
power = int(input("ENTER POWER OF THE  NUMBER ="))
# INITIALIZING IT BY 1 SO TO ELIMINATE GARBAGE VALUE
multiple = 1
for i in range(0, power):
    multiple = multiple * number
print(" POWER OF THE THE NUMBER IS =", multiple)
