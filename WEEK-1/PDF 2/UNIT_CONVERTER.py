print("*********************************************")
print("            UNIT CONVERTER                   ")
print("*********************************************")
# TAKING VALUE IN GRAM FROM THE USER
gram = input("ENTER VALUE IN GRAM ")
# TURNING GRAM TYPE INTO FLOAT
gram = float(gram)
# COMPARING FOR INVALID ENTRY
if (gram < 0):
    print("INVALID")
else:
    kg = gram/1000
    print(" VALUE IN KG IS =", kg)
