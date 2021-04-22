# UNIVERSITY MANAGEMENT SYSTEM
import os
name = []
matric = []
fsc = []
ecat = []
merit = []

os.system('cls' if os.name == 'nt' else 'clear')
# WE WILL APPLY THE LOOP IN ORDER TO RUN THE PROGRAM CONTINUESLY
program_running = True
while program_running == True:
    print("UNIVERSITY MANAGEMENT SYSTEM")
    print("SELECT ANY OF THE OPTION FROM THE FOLLOWING")
    print("1.TO ADD ANY STUDENT RECORD")
    print("2.VIEW ALL THE RECORDS")
    print("3.NAME AND MERIT OF THE TOP STUDENT")
    print("4.NAME AND MERIT OF THE BOTTOM STUDENT")
    print("5.EXIT")
    option = int(input(("ENTER YOUR OPTION =")))
    # adding if for the option camparison

    if option == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        name.append(input("ENTER NAME OF THE STUDENT ="))
        matric_temp = float(input("ENTER MATRIC MARKS OF THE STUDENT =  "))
        matric.append(matric_temp)
        fsc_temp = float(input("ENTER FSC MARKS OF THE STUDENT =  "))
        fsc.append(fsc_temp)
        ecat_temp = float(input("ENTER ECAT MARKS OF THE STUDENT =  "))
        ecat.append(ecat_temp)
        # CALCULTING MERIT ANS STORING IT IN TEMP
        merit_temp = 25*(matric_temp/1100)+45*(fsc_temp/510)+30*(ecat_temp/400)
        merit.append(merit_temp)
        wait = input("RECORD HAS BEEN UPDATED ............")
        print("PRESS ANY KEY TO CONTINUE...........")
        os.system('cls' if os.name == 'nt' else 'clear')

    if option == 2:
        # USING LENGTH FUCNTION TO SEE HOW MANY ENTERIES ARE MADE IN  A ARRAY
        os.system('cls' if os.name == 'nt' else 'clear')
        total_enteries = len(name)
        print(" NAME ", "\t \t", "MATRIC MARKS", "\t \t",
              "FSC MARKS", "\t \t", "ECAT MARKS", "\t \t", "MERIT")
        for i in range(0, total_enteries):
            print(" ", name[i], "\t \t ", matric[i], "\t \t ",
                  fsc[i], "\t \t ", ecat[i], "\t \t ", merit[i])
        wait = input("PRESS ANY KEY TO CONTINUE..........")
        os.system('cls' if os.name == 'nt' else 'clear')

    if option == 3:
        # USING FOR LOOP TO EXTRACT THE STUDENT WITH HIGHEST MARKS
        os.system('cls' if os.name == 'nt' else 'clear')
        largest = -10000
        counter = 0
        highest_counter = 0
        for i in merit:
            if largest < i:
                largest = i
                highest_counter = counter
            counter = counter+1

        print("STUDENT HAVING THE HIGHEST MERIT IS ")
        print(name[highest_counter], "  ", matric[highest_counter], "  ",
              fsc[highest_counter], "  ", ecat[highest_counter], "  ", merit[highest_counter])
        # CREATED A RAW INPUT TO WAIT FOR SOME TIME SO WHEN USER PRESS ANY KEY IT COMES BACK TO MAIN SCREEN
        wait = input("PRESS ANY KEY TO CONTINUE..........")
        os.system('cls' if os.name == 'nt' else 'clear')

    if option == 4:

        os.system('cls' if os.name == 'nt' else 'clear')
        smallest = merit[0]
        counter = 0
        lowest_counter = 0
        for i in merit:
            if smallest > i:
                smallest = i
                lowest_counter = counter
            counter = counter+1

        print("STUDENT HAVING THE LOWEST MERIT IS ")
        print(name[lowest_counter], "  ", matric[lowest_counter], "  ",
              fsc[lowest_counter], "  ", ecat[lowest_counter], "  ", merit[lowest_counter])
        # CREATED A RAW INPUT TO WAIT FOR SOME TIME SO WHEN USER PRESS ANY KEY IT COMES BACK TO MAIN SCREEN
        wait = input("PRESS ANY KEY TO CONTINUE..........")
        os.system('cls' if os.name == 'nt' else 'clear')

    if option == 5:
        program_running = False
