# LIST CONTANING THE EMPTY PART
list_1 = ["MIKE", "", "KELLY", "", "EMMA", "", "BRAD"]
# INITIALIZE A NEW LIST TO STORE THE DATA WITHOUT SPACE
new_list = []
# APPLYING LOOP
for i in list_1:
    if(i != ""):
        new_list.append(i)
print("NEW LIST WITHOUT SPACING IS ")
print(new_list)
