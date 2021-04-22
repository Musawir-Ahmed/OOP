# FIRST WE WILL MAKE CLASSES

'''
ACORDING TO THE GIVEN SENARIOS THEIR WILL BE 4 CLASSES WHICH INCLUDES
CUSTOMER
ITEMS
ORDER
PAYMENTS
'''

'''
ARRAYS
'''
product_record = []
order_record = []
customer_record = []
'''
'''

'''
CLASES
'''


class Product:
    __weight = ""
    detail = ""
    __stock = ""
    name = ""
    __price = 0
    tax = 0

    def __init__(self, name, detail):
        self.name = name
        self.detail = detail

    def set_stock(self, stock):
        stock = int(stock)
        if(stock > 0):
            self.__stock = stock
            return True
        else:
            return False

    def get_stock(self):
        return(self.__stock)

    def set_weight(self, weight):
        weight = float(weight)
        if(weight > 0):
            self.__weight = weight
            print(self.__weight)
            return True
        else:
            return False

    def get_weight(self):
        return(self.__weight)

    def set_cash(self, price):
        price = int(price)
        if(price > 0):
            self.__price = price
            self.tax = 0.05*price
            return True
        else:
            return False

    def get_price(self):
        return(self.__price)


class Customer:
    order_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def order_object(self, weight, detail, stock, name, price, tax, adress):
        order_object_making = Order(
            weight, detail, stock, name, price, tax, adress)
        self.order_list.append(order_object_making)


class Order:
    def __init__(self, weight, detail, stock, name, price, tax, adress):
        self.weight = weight
        self.detail = detail
        self.stock = stock
        self.name = name
        self.price = price
        self.tax = tax
        self.adress = adress


'''
'''


def item_check(product_name, adress, customer_object):
    for field in product_record:
        if field.name == product_name:
            customer_object.order_object(
                field.get_weight(), field.detail, field.get_stock(), field.name, field.get_price(), field.tax, address)


def header():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("****************************************************************")
    print("*               STORE MANAGEMENT SYSTEM                        *")
    print("****************************************************************")


def main_menu():
    header()
    print("1.LOGIN")
    print("2.SIGNUP FOR CUSTOMER")


def show_customer_order(customer_object):
    header()
    print("NAME\tSTOCK\tPRICE\tWEIGHT\tDETAIL\t\tTAX\tADRESS")
    for field in customer_object.order_list:
        print(field.name, "\t", field.stock, "\t", field.price, "\t",
              field.weight, "\t", field.detail, "\t", field.tax, "\t", field.adress)


def admin_menu():
    header()
    print(" WELCOME DEAR ADMIN ")
    print("1.TO ADD PRODUCT")
    print("2.TO VIE ALL PRODUCTS")
    print("3.TO VIEW ALL ORDERS")


def option1_admin():
    weight = ""
    detail = ""
    stock = ""
    name = ""
    price = ""
    product_object = ""
    stock_condition = True
    weight_condition = True
    price_condition = True
    name = input("ENTER NAME OF THE PRODUCT =")
    detail = input("ENTER DETAIL OF THE PRODUCT")
    stock = input("ENTER STOCK OF THE PRODUCT")
    weight = input("ENTER WIGHT OF THE PRODUCT IN KG")
    price = input("ENTER PRICE OF THE PRODUCT")
    product_object = Product(name, detail)
    price_condition = product_object.set_cash(price)
    weight_condition = product_object.set_weight(weight)
    stock_condition = product_object.set_stock(stock)

    header()
    if stock_condition == True and weight_condition == True and price_condition == True:
        product_record.append(product_object)
        print("PRODUCT ADDED SUCESSFULLY")
    if stock_condition == False:
        print("INVALID COMMAND TO ADD STOCK")
    if weight_condition == False:
        print("INVALID COMMAND TO ADD WEIGHT")
    if price_condition == False:
        print("INVALID COMMAND TO SET PRODUCT PRICE")
    input("PRESS ANY KEY TO CONTINUE...............")


def option2_admin():
    header()
    print("NAME\tSTOCK\tPRICE\tWEIGHT\tDETAILS")
    for field in product_record:
        print(field.get_price())
        print(field.name, "\t", field.get_stock(), "\t", field.get_price(),
              "\t", field.get_weight(), "KG", "\t\t", field.detail)
    input("PRESS ANY KEY TO CONTINUE.................")


def option3_admin():
    header()


def customer_menu():
    header()
    print("WELCOME DEAR CUTOMER")
    print("1.NEW ORDER")
    print("2.SEE ORDER")
    print("3.CHANGE PASSWORD")
    print("4.SHOPPING CART")
    print("5.LOGOUT")


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
            manager_option = 0
            while(manager_option != 4):
                admin_menu()
                manager_option = ""
                manager_option = int(input("ENTER OPTION NUMBER ="))
                if manager_option == 1:
                    option1_admin()
                if manager_option == 2:
                    option2_admin()
                if manager_option == 3:
                    option3_admin()
        else:
            for field in customer_record:
                if field.username == username and field.password == password:
                    customer_option = 0
                    while(customer_option != 5):
                        customer_menu()
                        customer_option = int(
                            input("ENTER OPTION NUMBER........"))
                        if customer_option == 1:
                            product_name = input(
                                "ENTER NAME OF THE PRODUCT       =")
                            address = input("SHIPING ORDER ADRESS  =")
                            item_check(product_name, address, field)
                        if customer_option == 2:
                            show_customer_order(field)
                            input("PRESS ANY KEY TO CONTINUE.....................")
    if option == 2:
        header()
        username = input("ENTER USER NAME FOR REGISTRATION =")
        password = input("ENTER PASSWORD FOR REGISTRATION =")
        customer_object = Customer(username, password)
        customer_record.append(customer_object)
        print("YOUR ACCOUNT HAS ADDED SUCESSFULLY ...............................")
        input("PRESS ANY KEY TO CONTINUE.........................................")
