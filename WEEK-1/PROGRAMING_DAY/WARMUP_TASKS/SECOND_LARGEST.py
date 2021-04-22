# NAKING A LIST TO TAKE A NUMBER AS A INPUT FROM THE USER
number = []
# using loop for the entery f data
for i in range(0, 10):
    number.append(int(input("ENTER A NUMBER =")))
number = sorted(number, reverse=True)
# AS WEKNOW THE LARGEST WILL ON THE FIRST INDEX THAT IS 0 AND SECOND LARGEST ON 1 SO
print("SECOND LARGEST NUMBER IN THE LIST IS ", number[1])
