import os

# DECLARING A OST TO STORE PRODUCT DATA
productrecord = []

# DECLARING CLASS


class productinfo:
    ProductId = 0
    Name = ""
    Price = 0
    Category = ""
    Brandname = ""
    Country = ""


# HEADER FUNCTION
def header():
    print("**************************************************************************\n")
    print("                               PRODUCT  RECORD                            \n")
    print("**************************************************************************\n")
    print("--------------------------------------------------------------------------\n")


# OPTIONS DISPLAYING FUNCTION
def displayoptions():
    print("1.ADD PRODUCT")
    print("2.SHOW PRODUCT")
    print("3.TOTAL STORE WORTH")
    print("4.EXIT")


# ADD PRODUCT FUNCTON
def addproduct():
    product = productinfo()
    product.ProductId = int(input("ENTER PRODUCT ID ="))
    product.Name = input("ENTER NAME OF TJE PRODUCT =")
    product.Price = int(input("ENTER PRICE OF THE PRODUCT ="))
    product.Category = input("ENTER CATEGORY OF THE PRODUCT =")
    product.Brandname = input("ENTER BRAND NAME OF THE PRODUCT =")
    product.Country = input("ENTER NAME THE COUNTRY WHER PRODUCT PRODUCED =")
    return product


# CLEAR SCREEN FUNCTION
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# PRESS KEY TO CONTINUE FUNCTION
def presskey():
    input("PRESS ENTER TO CONTINUE.............")


# FUCNTION TO SHOW ALL THE PRODUCTS SAVED
def showproduct(productrecord):
    print("NAME\t ID \tPRICE\tCATEGORY\tBRAND\tCOUNTRY")
    for field in productrecord:
        print(field.ProductId, "\t", field.Name, "\t", field.Price, "\t",
              field.Category, "\t", field.Brandname, "\t", field.Country, "\n")


# PROGRSM TO SHOW PRODUCTS STORE
def totalworth(productrecord):
    totalworth = 0
    for field in productrecord:
        field.Price = int(field.Price)
        totalworth = totalworth+field.Price
    return totalworth


program_running = True
counter = 0

# MAIN LOOP
while program_running == True:

    clearscreen()
    header()
    displayoptions()
    option = int(input("ENTER OPTION NUMBER ="))
# OPTION 1 TO ADD PRODUCT
    if option == 1:
        clearscreen()
        record = addproduct()
        productrecord.append(record)
# OPTION 2 TO SHOW PRODUCTS
    if(option == 2):
        clearscreen()
        header()
        showproduct(productrecord)
        presskey()
# TO CALCULAYE TOTAL WORTH
    if(option == 3):
        worth = totalworth(productrecord)
        print("TOTAL WORTH OF THE STORE IS =", worth)
        presskey()
# TO TERMINATE PROGRAM
    if(option == 4):
        program_running = False
