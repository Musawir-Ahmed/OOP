# TAKING NUMBER OF CLASSES HELD AND NUMBER OF CLASSES ATTENDED BY THE USER
number_of_classes_held = float(input("ENTER NUMBER OF CLASSES HELD ="))
number_of_classes_attended = float(input("ENTER NUMBER OF CLASSES ATTENDED ="))
percentage = (number_of_classes_attended/number_of_classes_held)*100
# PRINTING THE ATTENDING CLASSES PERCENTAGE
print("CLASSES ATTENDED PERCENTAGE IS =", percentage)
# COMPARING PERCENTAGE
if(percentage >= 75):
    print(" STUDENT IS ALLOWED TO SIT IN THE EXAM ")
else:
    print(" STUDENT IS NOT ALLOWED TO SIT IN THE EXAM ")
