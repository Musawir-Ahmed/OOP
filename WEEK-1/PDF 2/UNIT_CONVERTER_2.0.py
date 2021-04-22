# TAKING VALUE FROM THE USER
value = float(input(" ENTER VALUE TO CONVERT ="))
# TAKING THE VALUE UNIT IN WHICH THE VALUE IS FROM THE USER
value_unit = input(" ENTER VALUE UNIT ")
# TAKING THE VALUE UNIT N WHICH WE HAVE TO CONVERT THE VALUE
value_unit_convert = input(" ENTER VALUE UNIT TO CONVERT INTO  ")
# DECLARING BOOL VARIABLE
condition = False
# COMPARING ACCORDING TO THE GIVEN VALUE AND TO WHICH WE HAVE TO CONVERT A VALUE
if(value_unit == "GRAM" and value_unit_convert == "KG"):
    converted_value = value/1000
    condition = True
elif(value_unit == "KG" and value_unit_convert == "GRAM"):
    converted_value = value*1000
    condition = True
elif(value_unit == "METER" and value_unit_convert == "CENTIMETER"):
    converted_value = value*100
    condition = True
elif(value_unit == "CENTIMETER" and value_unit_convert == "METER"):
    converted_value = value/100
    condition = True
elif(value_unit == "SECOND" and value_unit_convert == "HOURS"):
    converted_value = value/3600
    condition = True
elif(value_unit == "USD" and value_unit_convert == "PKR"):
    converted_value = value*180
    condition = True
if(condition == True):
    print(value, " ", value_unit, " IN ",
          value_unit_convert, " IS ", converted_value)
    print("CONVERTED VALUE IS =", converted_value)
else:
    print("INVALID ENTRY")
