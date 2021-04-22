import os


class productinfo:
    ProductId = 0
    Name = ""
    Price = 0
    Category = ""
    Brandname = ""
    Country = ""


def header():
    print("**************************************************************************\n")
    print("                               PRODUCT  RECORD                            \n")
    print("**************************************************************************\n")
    print("--------------------------------------------------------------------------\n")


def displayoptions():
    print("1.ADD PRODUCT")
    print("2.SHOW PRODUCT")
    print("3.TOTAL STORE WORTH")
    print("4.EXIT")


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def presskey():
    input("PRESS ENTER TO CONTINUE.............")


def showproduct(product1, product2, product3):
    print("NAME\t ID \tPRICE\tCATEGORY\tBRAND\tCOUNTRY")
    if(product1.Name != ""):
        print(product1.Name, "\t", product1.ProductId, "\t", product1.Price, "\t",
              product1.Category, "\t", product1.Brandname, "\t", product1.Country)

    if(product2.Name != ""):
        print(product2.Name, "\t", product2.ProductId, "\t", product2.Price, "\t",
              product2.Category, "\t", product2.Brandname, "\t", product2.Country)

    if(product3.Name != ""):
        print(product3.Name, "\t", product3.ProductId, "\t", product3.Price, "\t",
              product3.Category, "\t", product3.Brandname, "\t", product3.Country)


program_running = True
counter = 0


product1 = productinfo()
product2 = productinfo()
product3 = productinfo()


while program_running == True:

    clearscreen()
    header()
    displayoptions()
    option = int(input("ENTER OPTION NUMBER ="))
    if option == 1:
        clearscreen()
        header()
        if(counter == 0):
            product1.ProductId = int(input("ENTER PRODUCT ID ="))
            product1.Name = input("ENTER PRODUCT NAME =")
            product1.Category = input("ENTER PRODUCT CATEGORY =")
            product1.Brandname = input("ENTER PRODUCTS BRAND NAME =")
            product1.Country = input("ENTER NAME OF THE PRODUCT COUNTRY")
            product1.Price = int(input("ENTER PRICE OF THE PRODUCT"))

        if(counter == 1):
            product2.ProductId = int(input("ENTER PRODUCT ID ="))
            product2.Name = input("ENTER PRODUCT NAME =")
            product2.Category = input("ENTER PRODUCT CATEGORY =")
            product2.Brandname = input("ENTER PRODUCTS BRAND NAME =")
            product2.Country = input("ENTER NAME OF THE PRODUCT COUNTRY")
            product2.Price = int(input("ENTER PRICE OF THE PRODUCT"))

        if(counter == 2):
            product3.ProductId = int(input("ENTER PRODUCT ID ="))
            product3.Name = input("ENTER PRODUCT NAME =")
            product3.Category = input("ENTER PRODUCT CATEGORY =")
            product3.Brandname = input("ENTER PRODUCTS BRAND NAME =")
            product3.Country = input("ENTER NAME OF THE PRODUCT COUNTRY")
            product3.Price = int(input("ENTER PRICE OF THE PRODUCT"))

            counter = 0
        presskey()
        counter = counter+1

    if(option == 2):
        clearscreen()
        header()
        showproduct(product1, product2, product3)
        presskey()

    if(option == 3):
        totalworth = int(product1.Price) + \
            int(product2.Price)+int(product3.Price)
        print("TOTAL WORTH OF THE STORE IS =", totalworth)
        presskey()
