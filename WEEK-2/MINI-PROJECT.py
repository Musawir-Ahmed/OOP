# STORE MANAGEMENT SYSTEM
import os
product_record = ['APPLE,FRUIT,23,34,5,', 'MANGO,FRUIT,65,76,7,']
selling_record = []
all_tax = 0

# FUNCTION TO DISPLAY THE TOP HEADER


def show_header():
    print("*************************************************************************************")
    print("\n")
    print("                                STORE MANAGEMENT SYSTEM                                            ")
    print("\n")
    print("*************************************************************************************")
    print("\n")

# FUNCTION TO DISPLAY THE MAIN OPTIONS


def show_menu():
    print("1.ADD PRODUCT")
    print("2.VIEW ALL PRODUCTS")
    print("3.FIND PRODUCT WITH HIGHEST UNIT PRICE")
    print("4.VIEW SALE TAX OF ALL PRODUCTS")
    print("5.BUY PRODUCT")
    print("6.PRODUCT TO BE ORDERED")
    print("7.EXIT")
    print("ENTER OPTION NUMBER...=")


# FUNCTION TO DISPLAY SU  HEADER
def show_subheader():
    print("---------------------------------------------------------------------------------------")


def addproduct_list(product_name, product_category, product_price, product_stock, product_minimumstock):
    # CONCATINATING ALL THE RECORD IN IRDER TO SAVE IT IN THE LIST
    record = product_name+","+product_category+"," + \
        product_price+","+product_stock+","+product_minimumstock+","+","
    product_record.append(record)


def addproductui():
    product_name = input("ENTER NAME OF THE PRODUCT =")
    product_category = input("ENTER PRODUCT CATEGORY GROCERY / FRUIT :")
    product_price = input("ENTER PRODUCT PRICE =")
    product_stock = input("ENTER PRODUCT STOCK =")
    product_minimumstock = input("ENTER PRODUCT MINIMUM STOCK =")
    addproduct_list(product_name, product_category,
                    product_price, product_stock, product_minimumstock)


def view_product():
    global product_record
    print("PRODUCT \t CATEGORIES \t PRICE \t STOCK \t MINIMUM STOCK")
    # APPLYRIN FOR LOOP TO SEPERATE THE ATTRIBUTES
    for field in product_record:
        temp_name = get_field(field, 1)
        temp_category = get_field(field, 2)
        temp_price = get_field(field, 3)
        temp_stock = get_field(field, 4)
        temp_minimum_stock = get_field(field, 5)
        print(temp_name, "\t\t  ", temp_category, "\t ", temp_price,
              "\t ", temp_stock, "\t ", temp_minimum_stock)
        print("\n")


def get_field(field, commano):
    global product_record
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


def get_high_priced_product():
    largest = -10000
    counter = 0
    largest_idx = 0

    for field in product_record:
        temp_price = get_field(field, 3)
        temp_price = int(temp_price)
        if(largest < temp_price):
            largest = temp_price
            largest_idx = counter
        counter = counter+1

    field = product_record[largest_idx]

    temp_name = get_field(field, 1)
    temp_category = get_field(field, 2)
    temp_price = get_field(field, 3)
    temp_stock = get_field(field, 4)
    temp_minimum_stock = get_field(field, 5)

    print("PRODUCT \t CATEGORIES \t PRICE \t STOCK \t MINIMUM STOCK")
    print(temp_name, "\t\t ", temp_category, "\t  \t ", temp_price,
          "\t  ", temp_stock, "\t  ", temp_minimum_stock)


def buy_product():

    global product_record
    total_sales_tax = 0
    global selling_record
    global all_tax
    total_bill = 0
    total_no = int(input("ENTER NUMBER OF PRODUCTS YOU WANT TO BUY ="))

    for i in range(0, total_no):
        product_found = False
        counter = 0
        product_idx = 0
        cal_price = 0
        new_stock = 0
        record = ""

        product_name = input("ENTER PRODUCT NAME YOU WANT TO BUY =")
        product_quantity = int(input("ENTER QUANTITY ="))

        for field in product_record:
            temp_name = get_field(field, 1)
            temp_category = get_field(field, 2)
            temp_price = int(get_field(field, 3))
            temp_stock = int(get_field(field, 4))

            if(product_name == temp_name and product_quantity > temp_stock):
                product_found = True
                print("PRODUCTIVE QUANTITY IS LOW THAN ASKED QUANTITY ")
                print(temp_stock, " ", temp_name, " ARE AVAILABLES")

            if(product_name == temp_name and product_quantity <= temp_stock):
                product_found = True
                product_idx = counter
                cal_price = product_quantity*temp_price

                if(temp_category == "FRUIT"):
                    sales_tax = 0.05*cal_price
                    sales_tax = str(sales_tax)

                if(temp_category == "GROCERIES"):
                    sales_tax = 0.1*cal_price
                    sales_tax = str(sales_tax)

                if(temp_category != "FRUIT" and temp_category != "GROCERIES"):
                    sales_tax = 0.05*cal_price
                    sales_tax = str(sales_tax)

                cal_price = str(cal_price)
                temp_price = str(temp_price)
                product_quantity = str(product_quantity)

                record = product_name+","+product_quantity+"," + \
                    temp_price+","+cal_price+","+sales_tax+","

                selling_record.append(record)
                temp_stock = int(temp_stock)
                product_quantity = int(product_quantity)
                new_stock = temp_stock-product_quantity

                record = product_record[product_idx]

                temp_name = get_field(record, 1)
                temp_category = get_field(record, 2)
                temp_price = get_field(record, 3)
                temp_stock = int(get_field(record, 4))
                temp_minimum_stock = get_field(record, 5)
                temp_stock = new_stock
                temp_stock = str(temp_stock)

                record = temp_name+","+temp_category+"," + temp_price + \
                    ","+temp_stock+","+temp_minimum_stock+","
                product_record[counter] = record

            counter = counter+1

        if(product_found == False):
            print("PRODUCT DOES NOT EXIT")

    product_price = 0
    print("PRODUCT NAME \t  PRODUCT QUANTITY \t  PRODUCT PRICE \t  TOTAL PRICE \t SALES TAX")

    for field in selling_record:
        product_name = get_field(field, 1)
        product_quantity = get_field(field, 2)
        product_price = get_field(field, 3)
        cal_price = get_field(field, 4)
        sales_tax = get_field(field, 5)
        total_bill = total_bill+int(cal_price)
        print(product_name, "\t\t\t", product_quantity, "\t\t\t",
              temp_price, "\t\t\t", cal_price, "\t  ", sales_tax)
        sales_tax = float(sales_tax)
        total_sales_tax = total_sales_tax+sales_tax
        all_tax = all_tax+total_sales_tax
        sales_tax = str(sales_tax)

    selling_record = []
    print("TOTAL SALE TAX INCLUDED IN THI BILL IS =", total_sales_tax)
    print("TOTAL BILL IS =", total_bill)


def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_key():
    wait = input(" PRESS ANY KEY TO CONTINUE ....................")


def order_product():

    print("PRODUCT \t CATEGORIES \t PRICE \t STOCK \t MINIMUM STOCK \t TRESHOLD")
    treshold = 0
    treshold = int(treshold)

    for field in product_record:
        treshold = 0
        temp_name = get_field(field, 1)
        temp_category = get_field(field, 2)
        temp_price = get_field(field, 3)
        temp_stock = int(get_field(field, 4))
        temp_minimum_stock = int(get_field(field, 5))

        if(temp_minimum_stock >= temp_stock):
            treshold = 1

        print(temp_name, "\t\t  ", temp_category, "\t ", temp_price,
              "\t ", temp_stock, "\t     ", temp_minimum_stock, "\t   ", treshold)


program_running = True

while program_running == True:
    screen_clear()
    show_header()
    show_menu()
    option = int(
        input("....................................................="))

    show_subheader()

    if option == 1:
        screen_clear()
        show_header()
        show_subheader()
        addproductui()
        press_key()
        screen_clear()

    if option == 2:
        screen_clear()
        show_header()
        show_subheader()
        view_product()
        press_key()
        screen_clear()

    if option == 3:
        screen_clear()
        show_header()
        show_subheader()
        get_high_priced_product()
        press_key()
        screen_clear()

    if option == 4:
        screen_clear()
        show_header()
        show_subheader()
        print("TOTAL SALE TAX IS =", all_tax)
        press_key()

    if option == 5:
        screen_clear()
        show_header()
        show_subheader()
        buy_product()
        press_key()
        screen_clear()

    if(option == 6):
        screen_clear()
        show_header()
        show_subheader()
        order_product()
        press_key()

    if option == 7:
        program_running = False
