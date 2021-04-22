# STORE MANAGEMENT SYSTEM
import os
productrecord = []
selling_record = []
all_tax = 0

# function call to display the menue


def show_header():
    print("*************************************************************************************")
    print("\n")
    print("                                STORE MANAGEMENT SYSTEM                                            ")
    print("\n")
    print("*************************************************************************************")
    print("\n")

# to showmenue


def show_menu():
    print("1.ADD PRODUCT")
    print("2.VIEW ALL PRODUCTS")
    print("3.FIND PRODUCT WITH HIGHEST UNIT PRICE")
    print("4.VIEW SALE TAX OF ALL PRODUCTS")
    print("5.BUY PRODUCT")
    print("6.PRODUCT TO BE ORDERED")
    print("7.EXIT")
    print("ENTER OPTION NUMBER...=")

# to show subheadings


def show_subheader():
    print("---------------------------------------------------------------------------------------")


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# PRESS KEY TO  CONTINUE FUNCTION
def presskey():
    input("PRESS ENTER TO CONTINUE.............")


# class to add product
class Addproduct:
    name = ""
    category = ""
    price = 0
    quantity = 0
    minimumquantity = 0
    treshold = 1

# CLASS FOR BUY PRODUCT


class Buyproduct:
    name = ""
    quantity = 0
    bill = 0
    category = ""


# functin to add product
def addproduct():
    product = Addproduct()
    product.name = input("ENTER NAME OF THE PRODUCT =")
    product.category = input("ENTER CATEGORY OF THE PRODUCT =")
    product.price = int(input("ENTER PRICE OF THE PRODUCT ="))
    product.quantity = int(input("ENTER QUANTITY OF THE PRODUCT ="))
    product.minimumquantity = int(
        input("ENTER MINIMUM QUATITY OF  THE PRODUCT ="))
    return product


# program to show product
def showproduct(productrecord):
    # TO DISPLAY NAME PRICE AND ALL THE RELEVENT DATA STORED IN THE PROGRAM
    print("NAME\tCATEGORY\tPRICE\tQUANTITY\tMINIMUM QUANTITY")
    for field in productrecord:
        print(field.name, "\t", field.category, "\t\t", field.price,
              "\t  ", field.quantity, "\t\t", field.minimumquantity, "\n")

# TO SORT TH HISGEST PRICE PRODUCT


def highestprice(productrecord):
    largest = -1000
    largestidx = 0
    counter = 0
    print("NAME\tCATEGORY\tPRICE\tQUANTITY\tMINIMUM QUANTITY")
# TO GET ATTRIBUTES OF AN IOBJECT STORED IN AN LIST
    for field in productrecord:
        if largest < float(field.price):
            largest = float(field.price)
            largestidx = counter
        counter = counter+1
    print(productrecord[largestidx].name, "\t", productrecord[largestidx].category, "\t\t", productrecord[largestidx].price,
          "\t", productrecord[largestidx].quantity, "\t\t", productrecord[largestidx].minimumquantity, "\n")

# FUNCTION THAT TAKES INPUT WITH THE HELP OF THE CLASS AND RETURNING THAT OBJECT


def buyproduct_input():
    entry = Buyproduct()
    entry.name = input("ENTER NAME OF THE PRODUCT =")
    entry.quantity = int(input("ENTER QUATITY OF TE PRODUCT ="))
    entry.category = input("ENTER CATEGORY OF THE PRODUCT =")
    return entry

# FUNCTION TO DISPLAY ALL THE SALES TAX


def salestax():
    print("TOTAL SALES TAX IS =", all_tax)

# FUNCTION THAT TAKE ENTRY THAT IS THE OBJECT OF THE CLASS THAT ENTER DATA TO BUY AND RETURN THAT OBJECT THAT OBJECT IS ENRED IN THIS FUNCTION AND PRPDUCT RECORD ARRAY IS ALSO ENTERED


def buyingprocess(entry, productrecord):
   # PROGRAM TO CALCULATE THE BILL ACCORDING TO THE GIVEN CONDITIONS
    bill = int(0)
    temp = int(0)
    global all_tax
    condition = False
    for field in productrecord:

        if (field.name == entry.name):
            condition = True
            if(float(field.quantity >= entry.quantity)):
                field.quantity = field.quantity-entry.quantity
                bill = entry.quantity*field.price
                if entry.category == "FRUIT":
                    temp = 0.05*bill
                if entry.category == "GROCERY":
                    temp = 0.01*bill
                if entry.category != "FRUIT" and entry.category != "GROCERY":
                    temp = 0.15*bill
                all_tax = all_tax+temp

                print("PRODUCT IS BUYED SUCESSFULLY.............")
                print("TOATAL BILL IS =", bill)
                print("SALES TAX INCLUDED IN IT =", all_tax)
            else:
                print("PRODUCT QUANTITY IS LOW ......")
    if condition == False:
        print("NO SUCH PRODUCT EXITS ........")

# FUNCTION TO TELL THAT WHIXH PRODUCT IS NEEDED TO BUY


def treshold(productrecord):
    print("NAME\tCATEGORY\tPRICE\tQUANTITY\tMINIMUM QUANTITY\tTRESHOLD")
    for field in productrecord:

        if float(field.minimumquantity <= field.quantity):
            field.treshold = 0

        print(field.name, "\t", field.category, "\t\t", field.price,
              "\t", field.quantity, "\t\t", field.minimumquantity, "\t\t\t", field.treshold, "\n")


# main loop
productrunning = True
while(productrunning != False):
    clearscreen()
    show_header()
    show_menu()
    show_subheader()
    option = int(input("ENTER OPTION NUMBER ="))
    if option == 1:
        clearscreen()
        show_header()
        show_subheader()
        record = addproduct()
        productrecord.append(record)
        print("PRODUCT HAS BEEN ADDED SUCESSFULLY ..........")
        presskey()
    if option == 2:
        clearscreen()
        show_header()
        show_subheader()
        showproduct(productrecord)
        presskey()
    if option == 3:
        clearscreen()
        show_header()
        show_subheader()
        highestprice(productrecord)
        presskey()
    if option == 4:
        clearscreen()
        show_header()
        show_subheader()
        salestax()
        presskey()
    if option == 5:
        clearscreen()
        show_header()
        show_subheader()
        entry = buyproduct_input()
        buyingprocess(entry, productrecord)
        presskey()
    if option == 6:
        clearscreen()
        show_header()
        show_subheader()
        treshold(productrecord)
        presskey()
