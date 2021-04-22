# FIRST WE WILL MAKE CLASSES

'''
ACORDING TO THE GIVEN SENARIOS THEIR WILL BE 4 CLASSES WHICH INCLUDES
CUSTOMER
ITEMS
ORDER
PAYMENTS
'''


def header():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("****************************************************************")
    print("*               STORE MANAGEMENT SYSTEM                        *")
    print("****************************************************************")


def main_menu():
    header()
    print("1.LOGIN")
    print("3.SIGNUP FOR CUSTOMER")


def admin_menu():
    header()
    print(" WELCOME DEAR ADMIN ")
    print("1.TO ADD PRODUCT")
    print("2.TO VIE ALL PRODUCTS")
    print("3.TO VIEW ALL ORDERS")


condition = True
while(condition == True):
    username = ""
    password = ""
    main_menu()
    option = int(input("ENTER OPTION NUMBER = "))
    if option == 1:
        username = input("ENTER YoUR USER NAME =")
        password = input("ENTER YOUR PASSWORD =")
        if username == "MANAGER123" and password == "OK12":
            admin_menu()
            manager_option = ""
            manager_option = int(input("ENTER OPTION NUMBER ="))
            if manager_option == 1:
                print("HELLO")
