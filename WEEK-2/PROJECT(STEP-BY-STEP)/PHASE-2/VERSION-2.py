import os
account_activation1 = 1
account_activation2 = 1
employe_id1 = ""
employe_id2 = ""
employe_password1 = ""
employe_password2 = ""
account_no1 = int(227771)
customar_pin1 = int(0)
customar_name1 = ""
customar_phonenumber1 = ""
customar_address1 = ""
customer_nationality1 = ""
customer_cnic1 = ""
account_no2 = int(227772)
customar_pin2 = int(0)
customar_name2 = ""
customar_phonenumber2 = ""
customar_address2 = ""
customer_nationality2 = ""
customer_cnic2 = ""
customar_cash1 = int(0)
customar_cash2 = int(0)
employe_experience1 = int(0)
employe_experience2 = int(0)

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

                if(option == 1):

                    os.system('cls' if os.name == 'nt' else 'clear')
                    account_no = input(
                        "ENTER ACCOUNT NUMBER OF THE CUSTOMER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")
                    condition = False
                    if account_no == customar_accountno1 and cnic == customer_cnic1:
                        account_activation1 = 0
                        print("ACCOUNT HAS BEEN DEACTIVATED.........")
                        condition = True
                    elif account_no == customar_accountno2 and cnic == customer_cnic2:
                        account_activation2 = 0
                        print("ACCOUNT HAS BEEN DEACTIVATED.........")
                        condition = True
                    elif condition == False:
                        print("ACCOUNT DOESNT EXIT PLEASE TRY AGAIN ..........")

                if(option == 2):
                    os.system('cls' if os.name == 'nt' else 'clear')

                    condition = False
                    # checking which employe variable is free
                    if employe_id1 == "":
                        employe_id1 = input("ENTER ID OF THE EMPLOYE =")
                        employe_password1 = input(
                            "ENTER PASSWORD OF THE EMPLOYE =")
                        employe_experience1 = input(
                            "ENTER EXPERIENCE OF THE EMPLOYE =")
                        condition = True
                    elif employe_id2 == "":
                        employe_id2 = input("ENTER ID OF THE EMPLOYE =")
                        employe_password2 = input(
                            "ENTER PASSWORD OF THE EMPLOYE =")
                        employe_experience2 = input(
                            "ENTER EXPERIENCE OF THE EMPLOYE =")
                        condition = True
                    elif condition == False:
                        print("EMPLOYE SPACE IS FULL...................")

                if(option == 3):
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("FOLOWING ARE THE NAMES OF YOUR EMPLOYES \n")
                    print("EMPLOYE ID                   PASSWORD    \n")
                    print(employe_id1, "      ", "      ", employe_password1)
                    print(employe_id2, "      ", "      ", employe_password2)

                if(option == 4):
                    os.system('cls' if os.name == 'nt' else 'clear')

                    employe_id = input("ENTER EMPLOYE ID =")
                    employe_password = input("ENTER PASSWORD OF THE EMPLOYE =")
                    condition = False
                    if employe_id == employe_id1 and employe_password == employe_password1:
                        employe_id1 = ""
                        employe_password1 = ""
                        condition = True
                    elif employe_id == employe_id2 and employe_password == employe_password2:
                        employe_id2 = ""
                        employe_password2 = ""
                        condition = True
                    elif condition == False:
                        print("EMPLOYE PASSWORD OR ID IS WRONG ........")

                if(option == 5):
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if (employe_experience1 >= employe_experience2):
                        print(employe_id1, "\n", employe_password1,
                              "\n", employe_experience1)
                    elif (employe_experience2 >= employe_experience1):
                        print(employe_id2, "\n", employe_password2,
                              "\n", employe_experience2)

                if(option == 6):
                    os.system('cls' if os.name == 'nt' else 'clear')

                    condition = False
                    employe_id = input("ENTER ID OF THE EMPLOYE =")
                    if employe_id == employe_id1:
                        employe_id1 = print("ENTER ID OF THE EMPLOYE =")
                        employe_password1 = print(
                            "ENTER PASSWORD OF THE EMPLOYE =")
                        employe_experience1 = input(
                            "ENTER EXPERIENCE OF THE EMPLOYE =")
                        condition = True
                    elif employe_id == employe_id2:
                        employe_id2 = print("ENTER ID OF THE EMPLOYE =")
                        employe_password2 = print(
                            "ENTER PASSWORD OF THE EMPLOYE =")
                        employe_experience2 = input(
                            "ENTER EXPERIENCE OF THE EMPLOYE =")
                        condition = True
                    elif condition == False:
                        print("EMPLOYE NOT FOUND.............")
        else:
            print("USERNAME OR PASSWORD IS INCORRECT....")
            input("PRESS ANY KEY TO CONTINUE............")
            os.system('cls' if os.name == 'nt' else 'clear')

    elif option == 2:
        print("WELCOME DEAR EMPLOYE")
        input("PRESS ANY KEY TO CONTINUE........")
        os.system('cls' if os.name == 'nt' else 'clear')
        tem_id = input("ENTER YOUR ID =")
        password = input("ENTER YOUR PASSWORD =")
        if tem_id == employe_id1 and employe_password1 == password or tem_id == employe_id2 and employe_password2 == password:
            while option != 8:
                print("MAIN MENU >> EMPLOYE >>")
                print("1.OPEN CUSTOMER BANK ACCOUNT")
                print("2.TO SEE CUSTOMER INFORMATION")
                print("3.TO CHANGE CUSTOMER PIN")
                print("4.TO DEPOSIT CUSTOMER CASH")
                print("5.TO CHANGE CUSTOMERS DETAILS")
                print("6.TO WITHDRAW CASH")
                print("7.TO CALCULATE PROFIT ON CASH")
                print("8.LOGOUT")
                option = int(input("ENTER OPTION NUMBER ="))
                os.system('cls' if os.name == 'nt' else 'clear')
                if option == 1:
                    if customar_name2 != "":
                        overwrite = int(input(
                            "ENTER 1 TO OVERWRITE CUSTOMER TO ADD NEW CUSTOMER ELSE ENTER 2 TO CANCEL"))
                        if(overwrite == 1):
                            customar_name1 = input(
                                "ENTER NAME OF THE CUSTOMER =")
                            customar_phonenumber1 = input(
                                "ENTER PHONE NUMBER OF THE CUSTOMER =")
                            customar_address1 = input(
                                "ENTER ADRESS OF THE CUSTOMER =")
                            customer_nationality1 = input(
                                "ENTER NATIONALITY OF THE CUSTOMER =")
                            customer_cnic1 = input(
                                "ENTER CNIC OF THE CUSTOMER =")
                            print("YOUR ACCOUN NUMBER IS =", account_no1)
                            customar_pin1 = input("ENTER YOUR PIN =")
                            print("YOUR ACCOUNT HAS BEEN OPENED SUCESSFULLY.......")
                    else:
                        customar_name2 = input(
                            "ENTER NAME OF THE CUSTOMER =")
                        customar_phonenumber2 = input(
                            "ENTER PHONE NUMBER OF THE CUSTOMER =")
                        customar_address2 = input(
                            "ENTER ADRESS OF THE CUSTOMER =")
                        customer_nationality2 = input(
                            "ENTER NATIONALITY OF THE CUSTOMER =")
                        customer_cnic2 = input("ENTER CNIC OF THE CUSTOMER =")
                        print("YOUR ACCOUN NUMBER IS =", account_no2)
                        customar_pin2 = input("ENTER YOUR PIN =")
                        print("YOUR ACCOUNT HAS BEEN OPENED SUCESSFULLY.......")
                if option == 2:
                    account_no = input("ENTER ACCOUNT NUMBER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")
                    if (account_no == account_no1 and cnic == customer_cnic1):
                        print("NAME =", customar_name1, "\n", "PHONE NUMBER =", customar_phonenumber1,
                              "\nADDRESS =", customar_address1, "\nCNIC =", customer_cnic1, "\nNATIONALITY =", customer_nationality1)
                    if (account_no == account_no2 and cnic == customer_cnic2):
                        print("NAME =", customar_name2, "\n", "PHONE NUMBER =", customar_phonenumber2,
                              "\nADDRESS =", customar_address2, "\nCNIC =", customer_cnic2, "\nNATIONALITY =", customer_nationality2)

                if option == 3:
                    account_no = input("ENTER ACCOUNT NUMBER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")
                    condition = False
                    if (account_no == account_no1 and cnic == customer_cnic1):
                        customar_pin1 == input("ENTER NEW PIN =")
                        condition = True
                        print("PIN HAS BEEN UPDATED....")

                    if (account_no == account_no2 and cnic == customer_cnic2):
                        customar_pin2 == input("ENTER NEW PIN =")
                        condition = True
                        print("PIN HAS BEEN UPDATED....")
                    elif condition == False:
                        print("ACCOUNT NUMBER OR PIN IS WRONG..............")
                    input("PRESS ANY KEY TO CONTNUE...........")

                if option == 4:
                    account_no = input("ENTER ACCOUNT NUMBER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")
                    pin = input("ENTER CUSTOMER PIN =")
                    cash = 0
                    condition = False
                    if (account_no == account_no1 and cnic == customer_cnic1 and pin == customar_pin1):
                        cash = int(input("ENTER AMMOUNT TO BE DEPOSIT ="))
                        customar_cash1 = cash+customar_cash1
                        condition = True
                    elif (account_no == account_no2 and cnic == customer_cnic2 and pin == customar_pin2):
                        cash = int(input("ENTER AMMOUNT TO BE DEPOSIT ="))
                        customar_cash2 = cash+customar_cash2
                        condition = True
                    elif condition == False:
                        print("ACCOUNT NUMBER OR PIN IS WRONG..............")
                    input("PRESS ANY KEY TO CONTNUE...........")

                if option == 5:
                    account_no = input("ENTER ACCOUNT NUMBER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")

                    if (account_no == account_no1 and cnic == customer_cnic1):
                        customar_name1 = input(
                            "ENTER NAME OF THE CUSTOMER =")
                        customar_phonenumber1 = input(
                            "ENTER PHONE NUMBER OF THE CUSTOMER =")
                        customar_address1 = input(
                            "ENTER ADRESS OF THE CUSTOMER =")
                        customer_nationality1 = input(
                            "ENTER NATIONALITY OF THE CUSTOMER =")
                        customer_cnic1 = input("ENTER CNIC OF THE CUSTOMER =")
                        print("YOUR ACCOUN NUMBER IS =", account_no1)
                        customar_pin1 = input("ENTER YOUR PIN =")
                    elif (account_no == account_no2 and cnic == customer_cnic2):
                        customar_name2 = input(
                            "ENTER NAME OF THE CUSTOMER =")
                        customar_phonenumber2 = input(
                            "ENTER PHONE NUMBER OF THE CUSTOMER =")
                        customar_address2 = input(
                            "ENTER ADRESS OF THE CUSTOMER =")
                        customer_nationality2 = input(
                            "ENTER NATIONALITY OF THE CUSTOMER =")
                        customer_cnic2 = input("ENTER CNIC OF THE CUSTOMER =")
                        print("YOUR ACCOUN NUMBER IS =", account_no1)
                        customar_pin2 = input("ENTER YOUR PIN =")
                if option == 6:
                    account_no = input("ENTER ACCOUNT NUMBER =")
                    cnic = input("ENTER CNIC OF THE CUSTOMER =")
                    pin = input("ENTER CUSTOMER PIN =")
                    cash = 0
                    condition = False
                    if (account_no == account_no1 and cnic == customer_cnic1 and pin == customar_pin1):
                        cash = int(input("ENTER AMMOUNT TO BE WITHDRAWED ="))
                        condition = True
                        if cash <= customar_cash1:
                            customar_cash1 = customar_cash1-cash
                            print("AMMOUNT HAS BEEN WITHDRAWED")
                            print("YOUR ACCOUNT BALANCE NOW IS =", customar_cash1)
                        else:
                            print(
                                "ACCOUNT BALANCE IS LESS THAN THE AMMOUNT TO BE WITHDRAWED")
                    elif (account_no == account_no2 and cnic == customer_cnic2 and pin == customar_pin2):
                        cash = int(input("ENTER AMMOUNT TO BE WITHDRAWED ="))
                        condition = True
                        if cash <= customar_cash2:
                            customar_cash2 = customar_cash2-cash
                            print("AMMOUNT HAS BEEN WITHDRAWED")
                            print("YOUR ACCOUNT BALANCE NOW IS =", customar_cash2)
                        else:
                            print(
                                "ACCOUNT BALANCE IS LESS THAN THE AMMOUNT TO BE WITHDRAWED")
                    elif condition == False:
                        print("SOME INFORMATION IS WRONG ORACCOUNT DOSNT EXIST")
                    input("PRESS ANY KEY TO CONTINUE....")

                if option == 7:
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
    elif option == 3:
        condition = False
        account_no = int(input("ENTER ACCOUNT NUMBER ="))
        pin = int(input("ENTER YOUR PINN ="))
        option = int(0)
        print(account_no1)
        while option != 5:
            if(account_no == account_no1 and pin == customar_pin1):
                condition = True
                print("MAIN MENU>>CUSTOMER")
                print("1.ACCOUNT DETAILS")
                print("2.CHECK BALANCE")
                print("3.FUND TRANSFER")
                print("4.BILL PAYMENT")
                print("5.LOGOUT")
                option = int(input("ENTER ANY OPTION  ="))
                if option == 1:
                    print("NAME =", customar_name1, "\nPHONE NUMBER =", customar_phonenumber1, "\nADRESS=", customar_address1,
                          "\nNATIONALITY =", customer_nationality1)
                if option == 2:
                    print("YOUR ACCOUNT BALANCE IS =", customar_cash1)
                if option == 3:
                    account_no = input(
                        "ENTER ACCOUNT NO YOU WANT TO TRANSFER =")
                    cash = int(input("ENTER AMMOUNT OF CASH"))
                    if account_no == account_no2:
                        if cash >= customar_cash1:
                            customar_cash1 = int(customar_cash1)
                            customar_cash2 = int(customar_cash2)
                            customar_cash1 = customar_cash1-cash
                            customar_cash2 = customar_cash2+cash
                            print("AMMOUNT HAS BEEN TRANSFERED SUCESSFULLY...")
                        else:
                            print(
                                "ACCOUNT BAANCE IS TO LOW FOR TRANSACTION \n YOUR ACCOUNT BALANCE IS =", customar_cash1)
                    else:
                        print("ACCOUNTNUMBER NOT FOUND OR MAT BE WRONG ")
                if option == 4:
                    print("ONLY WATER ELECTRICAL BILL CAN BE PAYED")
                    bill_type = input("ENTER BILL TYPE =")
                    cash = int(input("ENTER AMOUNT TO E PAYED ="))
                    if cash >= customar_cash1:
                        customar_cash1 = int(customar_cash1)
                        customar_cash1 = customar_cash1-cash
                        print("BILL HAS BEEN PAYED ")
                    else:
                        print(
                            "ACCOUNT BAANCE IS TO LOW FOR TRANSACTION \n YOUR ACCOUNT BALANCE IS =", customar_cash1)
            elif(account_no == account_no2 and pin == customar_pin2):
                condition = True
                print("MAIN MENU>>CUSTOMER")
                print("1.ACCOUNT DETAILS")
                print("2.CHECK BALANCE")
                print("3.FUND TRANSFER")
                print("4.BILL PAYMENT")
                print("5.LOGOUT")
                option = int(input("ENTER ANY OPTION  ="))
                if option == 1:
                    print("NAME =", customar_name2, "\nPHONE NUMBER =", customar_phonenumber2,
                          "\nADRESS=", customar_address2, "\nNATIONALITY =", customer_nationality2)
                if option == 2:
                    print("YOUR ACCOUNT BALANCE IS =", customar_cash2)
                if option == 3:
                    account_no = input(
                        "ENTER ACCOUNT NO YOU WANT TO TRANSFER =")
                    cash = int(input("ENTER AMMOUNT OF CASH"))
                    if account_no == account_no1:
                        if cash >= customar_cash2:
                            customar_cash2 = int(customar_cash2)
                            customar_cash1 = int(customar_cash1)
                            customar_cash2 = customar_cash2-cash
                            customar_cash1 = customar_cash1+cash
                            print("AMMOUNT HAS BEEN TRANSFERED SUCESSFULLY...")
                        else:
                            print(
                                "ACCOUNT BAANCE IS TO LOW FOR TRANSACTION \n YOUR ACCOUNT BALANCE IS =", customar_cash2)
                    else:
                        print("ACCOUNTNUMBER NOT FOUND OR MAT BE WRONG ")
                if option == 4:
                    print("ONLY WATER ELECTRICAL BILL CAN BE PAYED")
                    bill_type = input("ENTER BILL TYPE =")
                    cash = int(input("ENTER AMOUNT TO E PAYED ="))
                    if cash >= customar_cash2:
                        customar_cash2 = int(customar_cash2)
                        customar_cash2 = customar_cash2-cash
                        print("BILL HAS BEEN PAYED ")
                    else:
                        print(
                            "ACCOUNT BAANCE IS TO LOW FOR TRANSACTION \n YOUR ACCOUNT BALANCE IS =", customar_cash1)
        if condition == False:
            print("WRON ACCOUNT DETAILS ENTERED")
