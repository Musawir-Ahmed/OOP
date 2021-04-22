import os
customer_record = []
employe_record = ['Q,Q,1,']
customer_record = []
account_no = int(227771)


def header():
    print("**************************************************************************************************\n")
    print("                                      BANK MANAGEMENT SYSTEM                                      \n")
    print("**************************************************************************************************\n")
    print("---------------------------------------------------------------------------------------------------\n")


def welcome():
    print("WELCOME")


def main():
    print("MAIN")
    print("ENTER OPTION NUMBER TO LOGIN AS....")
    print("1-MANAGER")
    print("2-EMPLOYE")
    print("3-CUSTOMER")
    print("4-LOGOUT")


def manager():
    print("MAIN MENU>>MANAGER>>")
    print("1.ADD EMPLOYE")
    print("2.VIEW ALL EMPLOYE")
    print("3.DELETE EMPLOYE")
    print("4.VIEW EMPLOYE WITH LARGEST EXPERIENCES IN HIS/HER FIELD")
    print("5.CHANGE EMPLOYE DETAILS")
    print("6.LOGOUT")


def manager_security():
    condition = False
    username = input("ENTER YOUR USERNAME =")
    password = input("ENTER YOUR PASSWORD =")
    if username == "MUSAWIR_AHMED" and password == "1234":
        condition = True
    return condition


def get_field(field, commano):
    commano = int(commano)
    comma_counter = 0
    counter = 0
    diff = commano-1
    temp = ""

    while comma_counter < commano:

        if comma_counter >= diff and comma_counter < commano:
            temp = temp+field[counter]

        if(field[counter+1] == ","):
            comma_counter = comma_counter+1
            counter = counter+1

        counter = counter+1

    return temp


def employe_addition():
    global employe_record
    employe_id = input("ENTER NAME OF THE EMPLOYE  =")
    employe_password = input("ENTER PASSWORD OS THE EMPLOYE =")
    employe_experience = input(
        "ENTER EXPERIENCE OF THE EMPLOYE =")
    record = employe_id+","+employe_password+","+employe_experience+","
    employe_record.append(record)
    print("EMPLOYE HAS BEEN ADDED SUCESSFULLY.................")


def employe_display():
    print("EMPLOYE ID \t EMPLOYE PASSWORD \t EMPLOYE EXPERIENCE ")
    global employe_record
    for field in employe_record:
        if field != "":
            employe_id = get_field(field, 1)
            employe_password = get_field(field, 2)
            employe_experience = get_field(field, 3)
            if employe_id != "":
                print(employe_id, " \t ", employe_password,
                      " \t ", employe_experience)


def employe_deletion():
    global employe_record
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


def employe_experience():
    employe_experience_sorted = []
    employe_experience_list = []
    for field in employe_record:
        if field != "":
            employe_id = get_field(field, 1)
            employe_password = get_field(field, 2)
            employe_experience = get_field(field, 3)
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
        employe_experience_sorted.append(employe_record[largest_idx])
    print("EMPLOYE ID \t EMPLOYE PASSWORD \t EMPLOYE EXPERIENCE ")
    for field in employe_experience_sorted:
        employe_id = get_field(field, 1)
        employe_password = get_field(field, 2)
        employe_experience = get_field(field, 3)
        if employe_id != "":
            print(employe_id, " \t ", employe_password,
                  " \t ", employe_experience)


def change_employedetails():
    global employe_record
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
                employe_id = input("ENTER NAME OF THE EMPLOYE  =")
                employe_password = input(
                    "ENTER PASSWORD OS THE EMPLOYE =")
                employe_experience = input(
                    "ENTER EXPERIENCE OF THE EMPLOYE =")
                record = employe_id+","+employe_password+","+employe_experience+","
                employe_record[counter] = record

        counter = counter+1


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_key():
    input("PRESS ENTER TO CONTINUE................")


def employe_menue():
    print("MAIN MENU >> EMPLOYE >>")
    print("1.OPEN CUSTOMER BANK ACCOUNT")
    print("2.TO SEE CUSTOMER INFORMATION")
    print("3.TO CHANGE CUSTOMER PIN")
    print("4.TO DEPOSIT CUSTOMER CASH")
    print("5.TO CHANGE CUSTOMERS DETAILS")
    print("6.TO CALCULATE PROFIT ON CASH")
    print("7.LOGOUT")


def open_customeraccount():
    global customer_record
    global account_no
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


def customer_information():
    global customer_record
    account_no = input("ENTER ACCOUNT NUMBER OF THE USER =")
    cnic = input("ENTER CNIC OF THE USER =")
    for field in customer_record:
        if field != "":
            customer_name = get_field(field, 1)
            customer_phonenumber = get_field(field, 2)
            customer_address = get_field(field, 3)
            customer_nationality = get_field(field, 4)
            customer_cnic = get_field(field, 5)
            customer_accountno = get_field(field, 6)
            customer_pin = get_field(field, 7)
            customer_cash = get_field(field, 8)
            print(customer_accountno, customer_pin)
            if account_no == customer_accountno and cnic == customer_cnic:
                print("NAME =", customer_name, "\nPHONE NUMBER =", customer_phonenumber, "\nADDRESS =", customer_address, "\nNATIONALITY =",
                      customer_nationality, "\nCUSTOMER CNIC =", customer_cnic, "\nCUSTOMER ACCOUNT NUMBER =", customer_accountno, "\nPIN =", customer_pin)


def customer_pin():
    counter = 0
    global customer_record
    account_no = input("ENTER ACCOUNT NUMBER OF THE USER =")
    cnic = input("ENTER CNIC OF THE USER =")
    for field in customer_record:
        customer_name = get_field(field, 1)
        customer_phonenumber = get_field(field, 2)
        customer_address = get_field(field, 3)
        customer_nationality = get_field(field, 4)
        customer_cnic = get_field(field, 5)
        customer_accountno = get_field(field, 6)
        customer_pin = get_field(field, 7)
        customer_cash = get_field(field, 8)
        if account_no == customer_accountno and cnic == customer_cnic:
            customer_pin = input("ENTER NEW PIN =")
            record = customer_name+","+customer_phonenumber+","+customer_address+","+customer_nationality + \
                ","+customer_cnic+","+customer_accountno+","+customer_pin+","+customer_cash+","
            customer_record[counter] = record

        counter = counter+1


def deposit_cash():
    counter = 0
    global customer_record
    account_no = input("ENTER ACCOUNT NUMBER OF THE USER =")
    cnic = input("ENTER CNIC OF THE USER =")
    for field in customer_record:
        customer_name = get_field(field, 1)
        customer_phonenumber = get_field(field, 2)
        customer_address = get_field(field, 3)
        customer_nationality = get_field(field, 4)
        customer_cnic = get_field(field, 5)
        customer_accountno = get_field(field, 6)
        customer_pin = get_field(field, 7)
        customer_cash = get_field(field, 8)
        if account_no == customer_accountno and cnic == customer_cnic:
            temp = int(input("ENTER AMOUNT OF  CASH ="))
            customer_cash = int(customer_cash)
            customer_cash = customer_cash+temp
            customer_cash = str(customer_cash)
            record = customer_name+","+customer_phonenumber+","+customer_address+","+customer_nationality + \
                ","+customer_cnic+","+customer_accountno+","+customer_pin+","+customer_cash+","
            customer_record[counter] = record
        counter = counter+1


def change_details():
    counter = 0
    global customer_record
    account_no = input("ENTER ACCOUNT NUMBER OF THE USER =")
    cnic = input("ENTER CNIC OF THE USER =")
    for field in customer_record:
        customer_name = get_field(field, 1)
        customer_phonenumber = get_field(field, 2)
        customer_address = get_field(field, 3)
        customer_nationality = get_field(field, 4)
        customer_cnic = get_field(field, 5)
        customer_accountno = get_field(field, 6)
        customer_pin = get_field(field, 7)
        customer_cash = get_field(field, 8)
        if account_no == customer_accountno and cnic == customer_cnic:
            customer_name = input("ENTER NAME OF THE CUSTOMER =")
            customer_phonenumber = input(
                "ENTER PHONE NUMBER OF THE CUSTOMER =")
            customer_address = input("ENTER ADRESS OF THE CUSTOMER =")
            customer_nationality = input("ENTER NATONALITY OF THE CUSTOMER =")
            customer_cnic = input("ENTER CNIC OF THE CUSTOMER =")
            customer_accountno = input(
                "ENTER ACCOUNT NUMBER OF THE CUSTOMER =")
            customer_pin = input("ENTER PIN OF THE CUSTOMER =")
            record = customer_name+","+customer_phonenumber+","+customer_address+","+customer_nationality + \
                ","+customer_cnic+","+customer_accountno+","+customer_pin+","+customer_cash+","
            customer_record[counter] = record

        counter = counter+1


def profit():
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


def employe_security():
    global employe_record
    condition = False
    temp_id = input("ENTER EMPLOYE ID =")
    password = input("ENTER EMPLOYE PASSWORD =")
    for field in employe_record:
        if field != "":
            employe_id = get_field(field, 1)
            employe_password = get_field(field, 2)
            if temp_id == employe_id and password == employe_password:
                condition = True
    return condition


def customer_menue():
    print("MAIN MENU>>CUSTOMER")
    print("1.ACCOUNT DETAILS")
    print("2.CHECK BALANCE")
    print("3.BILL PAYMENT")
    print("4.LOGOUT")


def customer_security():
    global customer_record
    counter = 0
    condition = False
    index = 0
    account_no = input("ENTER ACCOUNT NUMBER OF THE USER =")
    pin = input("ENTER PIN OF YOUR ACCOUNT =")
    for field in customer_record:
        if field != "":
            customer_accountno = get_field(field, 6)
            customer_pin = get_field(field, 7)
        if account_no == customer_accountno and pin == customer_pin:
            condition = True
            index = counter
        counter = counter+1
    if condition == True:
        return index
    else:
        return -1


def account_details(counter):
    field = customer_record[counter]
    customer_name = get_field(field, 1)
    customer_phonenumber = get_field(field, 2)
    customer_address = get_field(field, 3)
    customer_nationality = get_field(field, 4)
    customer_cnic = get_field(field, 5)
    customer_accountno = get_field(field, 6)
    customer_pin = get_field(field, 7)
    customer_cash = get_field(field, 8)
    print("NAME =", customer_name, "\nPHONE NUMBER =", customer_phonenumber, "\nADDRESS =", customer_address, "\nNATIONALITY =",
          customer_nationality, "\nCUSTOMER CNIC =", customer_cnic, "\nCUSTOMER ACCOUNT NUMBER =", customer_accountno, "\nPIN =", customer_pin)


def check_balance(counter):
    field = customer_record[counter]
    customer_cash = get_field(field, 8)
    print("YOUR TOTAL ACCOUNT BALANCE IS =", customer_cash)


def bill_payment(counter):
    counter = 0
    global customer_record
    field = customer_record[counter]
    customer_name = get_field(field, 1)
    customer_phonenumber = get_field(field, 2)
    customer_address = get_field(field, 3)
    customer_nationality = get_field(field, 4)
    customer_cnic = get_field(field, 5)
    customer_accountno = get_field(field, 6)
    customer_pin = get_field(field, 7)
    customer_cash = get_field(field, 8)
    customer_cash = int(customer_cash)
    bill_type = input("ENTER BILL TYPE =")
    cash = int(input("ENTER AMOUNT TO BE PAYED ="))
    if(bill_type == "WATER" or bill_type == "ELECTRICITY"):
        if(customer_cash >= cash):
            customer_cash = customer_cash-cash
            print("BILL HAS BEEN PAYED SUCESSFULLY ")
        else:
            print("ACCOUNT BALANCE IS LOW")
    else:
        print("INVALID BILL TYPE ")
    customer_cash = str(customer_cash)
    record = customer_name+","+customer_phonenumber+","+customer_address+","+customer_nationality + \
        ","+customer_cnic+","+customer_accountno+","+customer_pin+","+customer_cash+","
    customer_record[counter] = record


program_running = True

while program_running == True:
    clear_screen()
    header()
    main()
    option = int(input("ENTER ANY OPTION ="))
    if(option == 1):
        condition = manager_security()
        if(condition == True):
            while option != 6:
                clear_screen()
                header()
                manager()
                option = int(input("ENTER ANY OPTION ="))
                if(option == 1):
                    clear_screen()
                    header()
                    employe_addition()
                    press_key()
                if(option == 2):
                    clear_screen()
                    header()
                    employe_display()
                    press_key()
                if(option == 3):
                    clear_screen()
                    header()
                    employe_deletion()
                    press_key()
                if(option == 4):
                    clear_screen()
                    header()
                    employe_experience()
                    press_key()
                if(option == 5):
                    clear_screen()
                    header()
                    change_employedetails()
                    press_key()
        else:
            print("USERNAME PASSWORD IS INCORRECT")
            press_key()
    elif option == 2:
        condition = employe_security()
        if condition == True:
            while option != 7:
                clear_screen()
                employe_menue()
                option = int(input("ENTER ANY OPTION  ="))
                if(option == 1):
                    clear_screen()
                    open_customeraccount()
                    press_key()
                if(option == 2):
                    clear_screen()
                    customer_information()
                    press_key()
                if(option == 3):
                    clear_screen()
                    customer_pin()
                    press_key()
                if(option == 4):
                    clear_screen()
                    deposit_cash()
                    print("RECORD HAS BEEN UPDATED")
                    press_key()
                if(option == 5):
                    clear_screen()
                    change_details()
                    print("RECORD HAS BEEN UPDATED")
                    press_key()
                if(option == 6):
                    clear_screen()
                    profit()
                    press_key()
        else:
            print("SOME INFORMATION YOU ENTERED IS WRONG")
            press_key()
    elif option == 3:
        condition = customer_security()
        if condition != -1:
            while option != 4:
                clear_screen()
                header()
                customer_menue()
                option = int(input("ENTER ANY OF THE OPTIONS  ="))
                if option == 1:
                    clear_screen()
                    header()
                    account_details(condition)
                    press_key()
                if option == 2:
                    clear_screen()
                    header()
                    check_balance(condition)
                    press_key()
                if option == 3:
                    clear_screen()
                    header()
                    bill_payment(condition)
                    press_key()
                if option == 4:
                    clear_screen()
                    header()
                    bill_payment(condition)
                    press_key()
