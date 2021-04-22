import os
customer_record = []
employe_record = []
customer_record = []
account_no = int(227771)
print("**************************************************************************************************\n")
print("                                      BANK MANAGEMENT SYSTEM                                      \n")
print("**************************************************************************************************\n")
print("---------------------------------------------------------------------------------------------------\n")
# OPTIONS AVAILABLE
program_running = True
while program_running == True:

    print("MAIN")
    print("ENTER OPTION NUMBER TO LOGIN AS....")
    print("1-MANAGER")
    print("2-EMPLOYE")
    print("3-CUSTOMER")
    print("4-LOGOUT")
    # getinh option number by the user
    option = int(input("ENTER OPYION NUMBER..........."))
    if(option == 1):
        manager_username = input("ENTER YOUR USER NAME =")
        manager_password = input("ENTER YOUR PASSWORD =")
        if manager_username == "MUSAWIR_AHMED" and manager_password == "1234":
            print("WELCOME DEAR MANAGER")
            input("PRESS ANY KEY TO CONTINUE.......")
            os.system('cls' if os.name == 'nt' else 'clear')
            # SHOWING MANAGER THE FOLLOWING OPTIONS
            while option != 7:
                print("MAIN MENU>>MANAGER>>")
                print("1.DEACVTIVATE OR ACTIVATE CUSTOMER ACCOUNT")
                print("2.ADD EMPLOYE")
                print("3.VIEW ALL EMPLOYE")
                print("4.DELETE EMPLOYE")
                print("5.VIEW EMPLOYE WITH LARGEST EXPERIENCES IN HIS/HER FIELD")
                print("6.CHANGE EMPLOYE DETAILS")
                print("7.LOGOUT")
                option = int(input("ENTER ANY OPTION ................"))
                # CAMPARING THE SELECTED OPTION
                if option == 2:
                    employe_id = input("ENTER NAME OF THE EMPLOYE  =")
                    employe_password = input("ENTER PASSWORD OS THE EMPLOYE =")
                    employe_experience = input(
                        "ENTER EXPERIENCE OF THE EMPLOYE =")
                    record = employe_id+","+employe_password+","+employe_experience+","
                    employe_record.append(record)
                    print("EMPLOYE HAS BEEN ADDED SUCESSFULLY.................")
                if option == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("EMPLOYE ID \t EMPLOYE PASSWORD \t EMPLOYE EXPERIENCE ")
                    for field in employe_record:
                        employe_id = ""
                        employe_experience = ""
                        employe_password = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != ","):
                                employe_id = employe_id+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                employe_password = employe_password+char
                            if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                                employe_experience = employe_experience+char

                            if(char == ","):
                                coma_counter = coma_counter+1
                        if employe_id != "":
                            print(employe_id, " \t ", employe_password,
                                  " \t ", employe_experience)
                    input("PRESS ENTER TO CONTINUE .........")

                if option == 4:
                    temp_employe_id = input("ENTER EMPLOYE ID =")

                    for field in employe_record:
                        counter = int(0)

                        employe_id = ""
                        employe_experience = ""
                        employe_password = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != ","):
                                employe_id = employe_id+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                employe_password = employe_password+char
                            if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                                employe_experience = employe_experience+char

                            if(char == ","):
                                coma_counter = coma_counter+1

                            if(temp_employe_id == employe_id):
                                employe_record[counter] = ""

                        counter = counter+1

                if option == 5:
                    employe_experience_sorted = []
                    employe_experience_list = []
                    for field in employe_record:
                        counter = int(0)
                        employe_experience = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                                employe_experience = employe_experience+char
                            if(char == ","):
                                coma_counter = coma_counter+1
                        employe_experience_list.append(int(employe_experience))
                    largest_idx_list = []
                    counter = 0
                    for field in range(0, len(employe_experience_list)):
                        largest = -100000
                        largest_idx = 0
                        counter = 0
                        for i in employe_experience_list:
                            if(largest < i):
                                largest = i
                                largest_idx = counter
                                counter = counter+1
                        employe_experience_list[largest_idx] = -1
                        employe_experience_sorted.append(
                            employe_record[largest_idx])
                    print("EMPLOYE ID \t EMPLOYE PASSWORD \t EMPLOYE EXPERIENCE ")
                    for field in employe_experience_sorted:
                        employe_id = ""
                        employe_experience = ""
                        employe_password = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != ","):
                                employe_id = employe_id+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                employe_password = employe_password+char
                            if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                                employe_experience = employe_experience+char

                            if(char == ","):
                                coma_counter = coma_counter+1
                        if employe_id != "":
                            print(employe_id, " \t ", employe_password,
                                  " \t ", employe_experience)
                    input("PRESS ENTER TO CONTINUE .........")
                if option == 6:
                    counter = 0
                    temp_employe = input("ENTER EMPLOYE ID =")
                    for field in employe_record:
                        employe_id = ""
                        employe_experience = ""
                        employe_password = ""
                        coma_counter = int(0)
                        for char in field:

                            if(coma_counter < 1 and char != ","):
                                employe_id = employe_id+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                employe_password = employe_password+char
                            if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                                employe_experience = employe_experience+char

                            if(char == ","):
                                coma_counter = coma_counter+1
                        if temp_employe == employe_id:
                            employe_id = input("ENTER NAME OF THE EMPLOYE  =")
                            employe_password = input(
                                "ENTER PASSWORD OS THE EMPLOYE =")
                            employe_experience = input(
                                "ENTER EXPERIENCE OF THE EMPLOYE =")
                            record = employe_id+","+employe_password+","+employe_experience+","
                            employe_record[counter] = record
                        counter = counter+1
    if option == 2:
        condition = False
        print("WELCOME DEAR EMPLOYE")
        input("PRESS ANY KEY TO CONTINUE........")
        os.system('cls' if os.name == 'nt' else 'clear')
        tem_id = input("ENTER YOUR ID =")
        password = input("ENTER YOUR PASSWORD =")
        for field in employe_record:
            employe_id = ""
            employe_experience = ""
            employe_password = ""
            coma_counter = int(0)
            for char in field:

                if(coma_counter < 1 and char != ","):
                    employe_id = employe_id+char
                if(coma_counter < 2 and char != "," and coma_counter == 1):
                    employe_password = employe_password+char
                if(coma_counter < 3 and char != "," and coma_counter != 1 and coma_counter == 2):
                    employe_experience = employe_experience+char

                if(char == ","):
                    coma_counter = coma_counter+1
            if tem_id == employe_id and password == employe_password:
                condition = True

        if condition == True:
            while option != 7:
                print("MAIN MENU >> EMPLOYE >>")
                print("1.OPEN CUSTOMER BANK ACCOUNT")
                print("2.TO SEE CUSTOMER INFORMATION")
                print("3.TO CHANGE CUSTOMER PIN")
                print("4.TO DEPOSIT CUSTOMER CASH")
                print("5.TO CHANGE CUSTOMERS DETAILS")
                print("6.TO CALCULATE PROFIT ON CASH")
                print("7.LOGOUT")
                option = int(input("ENTER OPTION NUMBER ="))

                if(option == 1):
                    name = input("ENTER YOUR NAME =")
                    phone_number = input("ENTER YOUR PHONE NUMBER =")
                    adress = input("ENTER CUSTOMER ADRESS =")
                    nationality = input("ENTER CUSTOMER NATIONALITY =")
                    cnic = input("ENTER CUSTOMER CNIC =")
                    print("YOU ACCOUNT NUMBER IS =", account_no)
                    pin = input("ENTER YOUR PIN =")
                    cash = input("ENTER CASH TO DEPOSIT =")
                    record = name+","+phone_number+","+adress+","+nationality + \
                        ","+cnic+","+str(account_no)+","+pin+","+cash+","
                    account_no = account_no+1
                    customer_record.append(record)
                    print("RECORD HAS BEEN UPDATED ")
                    input("PRESS ANY KEY TO CONTINUE...........")

                if(option == 2):
                    account_no = int(
                        input("ENTER ACCOUNT NUMBER OF THE USER ="))
                    cnic = int(input("ENTER CNIC OF THE USER ="))
                    condition = True
                    for field in customer_record:
                        customer_account_no = ""
                        customer_cnic = ""
                        customer_name = ""
                        customer_phonenumber = ""
                        customer_address = ""
                        customer_nationality = ""
                        customer_pin = ""
                        customer_cash = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != "," and coma_counter == 0):
                                customer_name = customer_name+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                customer_phonenumber = customer_phonenumber+char
                            if(coma_counter < 3 and char != "," and coma_counter == 2):
                                customer_address = customer_address+char
                            if(coma_counter < 4 and char != "," and coma_counter == 3):
                                customer_nationality = customer_nationality+char
                            if(coma_counter < 5 and char != "," and coma_counter == 4):
                                customer_cnic = customer_cnic+char
                            if(coma_counter < 6 and char != "," and coma_counter != 1 and coma_counter == 5):
                                customer_account_no = customer_account_no+char
                            if(coma_counter < 7 and char != "," and coma_counter != 1 and coma_counter == 6):
                                customer_pin = customer_pin+char
                            if(coma_counter < 8 and char != "," and coma_counter != 1 and coma_counter == 7):
                                customer_cash = customer_cash+char
                            if(char == ","):
                                coma_counter = coma_counter+1
                        customer_cnic = int(customer_cnic)
                        customer_account_no = int(customer_account_no)
                        if customer_cnic == cnic and customer_account_no == account_no:
                            print("NAME =", customer_name, "\nPHONE NUMBER =", customer_phonenumber, "\nADDRESS =", customer_address, "\nNATIONALITY =",
                                  customer_nationality, "\nCUSTOMER CNIC =", customer_cnic, "\nCUSTOMER ACCOUNT NUMBER =", customer_account_no, "\nPIN =", customer_pin)
                if option == 5:
                    account_no = int(
                        input("ENTER ACCOUNT NUMBER OF THE USER ="))
                    cnic = int(input("ENTER CNIC OF THE USER ="))
                    condition = True
                    counter = 0
                    for field in customer_record:
                        customer_account_no = ""
                        customer_cnic = ""
                        customer_name = ""
                        customer_phonenumber = ""
                        customer_address = ""
                        customer_nationality = ""
                        customer_pin = ""
                        customer_cash = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != "," and coma_counter == 0):
                                customer_name = customer_name+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                customer_phonenumber = customer_phonenumber+char
                            if(coma_counter < 3 and char != "," and coma_counter == 2):
                                customer_address = customer_address+char
                            if(coma_counter < 4 and char != "," and coma_counter == 3):
                                customer_nationality = customer_nationality+char
                            if(coma_counter < 5 and char != "," and coma_counter == 4):
                                customer_cnic = customer_cnic+char
                            if(coma_counter < 6 and char != "," and coma_counter != 1 and coma_counter == 5):
                                customer_account_no = customer_account_no+char
                            if(coma_counter < 7 and char != "," and coma_counter != 1 and coma_counter == 6):
                                customer_pin = customer_pin+char
                            if(coma_counter < 8 and char != "," and coma_counter != 1 and coma_counter == 7):
                                customer_cash = customer_cash+char
                            if(char == ","):
                                coma_counter = coma_counter+1
                        customer_cnic = int(customer_cnic)
                        customer_account_no = int(customer_account_no)
                        if customer_cnic == cnic and customer_account_no == account_no:
                            name = input("ENTER YOUR NAME =")
                            phone_number = input("ENTER YOUR PHONE NUMBER =")
                            adress = input("ENTER CUSTOMER ADRESS =")
                            nationality = input("ENTER CUSTOMER NATIONALITY =")
                            cnic = input("ENTER CUSTOMER CNIC =")
                            print("YOU ACCOUNT NUMBER IS =", account_no)
                            pin = input("ENTER YOUR PIN =")
                            cash = input("ENTER CASH TO DEPOSIT =")
                            customer_cnic = str(customer_cnic)
                            customer_account_no = str(customer_account_no)
                            record = name+","+phone_number+","+adress+","+nationality + \
                                ","+cnic+","+str(account_no) + \
                                ","+pin+","+cash+","
                            customer_record[counter] = record
                        counter = counter+1
                if option == 3:
                    account_no = int(
                        input("ENTER ACCOUNT NUMBER OF THE USER ="))
                    cnic = int(input("ENTER CNIC OF THE USER ="))
                    condition = True
                    counter = 0
                    for field in customer_record:
                        customer_account_no = ""
                        customer_cnic = ""
                        customer_name = ""
                        customer_phonenumber = ""
                        customer_address = ""
                        customer_nationality = ""
                        customer_pin = ""
                        customer_cash = ""
                        coma_counter = int(0)
                        for char in field:
                            if(coma_counter < 1 and char != "," and coma_counter == 0):
                                customer_name = customer_name+char
                            if(coma_counter < 2 and char != "," and coma_counter == 1):
                                customer_phonenumber = customer_phonenumber+char
                            if(coma_counter < 3 and char != "," and coma_counter == 2):
                                customer_address = customer_address+char
                            if(coma_counter < 4 and char != "," and coma_counter == 3):
                                customer_nationality = customer_nationality+char
                            if(coma_counter < 5 and char != "," and coma_counter == 4):
                                customer_cnic = customer_cnic+char
                            if(coma_counter < 6 and char != "," and coma_counter != 1 and coma_counter == 5):
                                customer_account_no = customer_account_no+char
                            if(coma_counter < 7 and char != "," and coma_counter != 1 and coma_counter == 6):
                                customer_pin = customer_pin+char
                            if(coma_counter < 8 and char != "," and coma_counter != 1 and coma_counter == 7):
                                customer_cash = customer_cash+char
                            if(char == ","):
                                coma_counter = coma_counter+1
                        customer_cnic = int(customer_cnic)
                        customer_account_no = int(customer_account_no)
                        if customer_cnic == cnic and customer_account_no == account_no:
                            pin = input("ENTER YOUR PIN =")
                        customer_cnic = str(customer_cnic)
                        customer_account_no = str(customer_account_no)
                        record = name+","+phone_number+","+adress+","+nationality + \
                            ","+cnic+","+str(account_no) + \
                            ","+pin+","+cash+","
                        customer_record[counter] = record
                        counter = counter+1
                if option == 6:
                    year = int(
                        input("ENTER YEAR IN WHICH YOU DEPOSITED AMMOUNT="))
                    ammount = int(input("ENTER AMMOUNT DEPOSITED ="))
                    # on every year 1% profit is generated on the deposited ammount
                    profit_percentage = 0
                    profit_percentage = year/100
                    profit = ammount*profit_percentage
                    print("YOU HAVE GOT THE PROFIT OF RS =", profit)
                    profit = ammount+profit
                    print("NOW YOUR AMMOUNT IN YOUR ACCOUNT IS=", profit)
    if option == 3:
        condition = False
        option = int(0)
        account_no = input("ENTER YOUR ACCOUNT NUMBER =")
        pin = input("ENTER YOUR PINN =")
        condition = True
        counter = 0
        for field in customer_record:
            customer_account_no = ""
            customer_cnic = ""
            customer_name = ""
            customer_phonenumber = ""
            customer_address = ""
            customer_nationality = ""
            customer_pin = ""
            customer_cash = ""
            coma_counter = int(0)
            for char in field:
                if(coma_counter < 1 and char != "," and coma_counter == 0):
                    customer_name = customer_name+char
                if(coma_counter < 2 and char != "," and coma_counter == 1):
                    customer_phonenumber = customer_phonenumber+char
                if(coma_counter < 3 and char != "," and coma_counter == 2):
                    customer_address = customer_address+char
                if(coma_counter < 4 and char != "," and coma_counter == 3):
                    customer_nationality = customer_nationality+char
                if(coma_counter < 5 and char != "," and coma_counter == 4):
                    customer_cnic = customer_cnic+char
                if(coma_counter < 6 and char != "," and coma_counter != 1 and coma_counter == 5):
                    customer_account_no = customer_account_no+char
                if(coma_counter < 7 and char != "," and coma_counter != 1 and coma_counter == 6):
                    customer_pin = customer_pin+char
                if(coma_counter < 8 and char != "," and coma_counter != 1 and coma_counter == 7):
                    customer_cash = customer_cash+char
                if(char == ","):
                    coma_counter = coma_counter+1

                if (account_no == customer_account_no and pin == customer_pin):
                    while option != 4:
                        print("MAIN MENU>>CUSTOMER")
                        print("1.ACCOUNT DETAILS")
                        print("2.CHECK BALANCE")
                        print("3.BILL PAYMENT")
                        print("4.LOGOUT")
                        option = int(input("ENTER OPTION NUMBER ="))
                        if option == 1:
                            print("NAME =", customer_name, "\nPHONE NUMBER =", customer_phonenumber, "\nADDRESS =", customer_address, "\nNATIONALITY =",
                                  customer_nationality, "\nCUSTOMER CNIC =", customer_cnic, "\nCUSTOMER ACCOUNT NUMBER =", customer_account_no, "\nPIN =", customer_pin)
                        if option == 2:
                            print("YOUR ACCOUNT BALANCE IS =", customer_cash)
                        if option == 3:
                            print("ONLY WATER  ELECTRICITY BILL CAN BE PAYED")
                            bill_type = input("ENTER BILL TYPE =")
                            cash = int(input("ENTER AMMOUNT TO BE PAYED ="))

                            if(bill_type == "WATER" or bill_type == "ELECTRICITY"):
                                if(customer_cash >= cash):
                                    customer_cash = int(customer_cash)
                                    customer_cash = customer_cash-cash
                                else:
                                    print("ACCOUNT BALANCE IS LOW")
                            else:
                                print("INVALID BILL TYPE ")
