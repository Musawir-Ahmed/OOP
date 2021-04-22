# TAKING MATRIC MARKS FSC MARKS AND ECAT MARKS AS THE INPUT FROM THE USER
matric_marks = float(input("ENTER YOUR MATRIC MARKS ="))
fsc_marks = float(input("ENTER YOUR FSC MARKS ="))
ecat_marks = float(input("ENTER YOUR ECAT MARKS ="))
# APPLYING FORMULA TO CALCULATE THE AGGREGATE
aggregate = (matric_marks/1100)*25+(fsc_marks/510)*45+(ecat_marks/400)*30
print("YOUR AGGREGATE IS =", aggregate)
