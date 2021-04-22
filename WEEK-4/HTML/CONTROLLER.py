# importing flask
from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")

product_record_list_temp = []
product_record_list_per = []


@ app.route("/")
def main():
    global product_record_list_temp
    length = int(len(product_record_list_temp))
    if length != 0:
        counter = 0
        return render_template("ADDPRODUCT.html", product=product_record_list_temp, counter=counter)

    return render_template("ADDPRODUCT.html")


@ app.route("/STORE")
def store():
    return render_template("STORE.html")


class Product:
    def __init__(self, produt_id, product_name, product_sale_price, product_purchase_price, product_stock):
        self.id = produt_id
        self.name = product_name
        self.sale_price = product_sale_price
        self.purchase_price = product_purchase_price
        self.stock = product_stock

    def store_record(self):
        myfile = open("PRODUCT.txt", "a")
        temp = self.id+","+self.name+","+self.sale_price + \
            ","+self.purchase_price+","+self.stock+","
        print(temp, file=myfile, sep="\n")
        myfile.close()


@app.route("/add_product_data", methods=['POST', 'GET'])
def data_add_product():
    global product_record_list_temp
    produt_id = request.form['ID']
    product_name = request.form['NAME']
    product_sale_price = request.form['SALE_PRICE']
    product_purchase_price = request.form['PURCHASE_PRICE']
    product_stock = str(0)
    record = Product(produt_id, product_name,
                     product_sale_price, product_purchase_price, product_stock)
    product_record_list_temp.append(record)
    length = int(len(product_record_list_temp))
    if length != 0:
        counter = 0
        return render_template("ADDPRODUCT.html", product=product_record_list_temp, counter=counter)

    return render_template("ADDPRODUCT.html")


@ app.route("/STORE_TO_FILE")
def store_record():
    global product_record_list_temp
    for field in product_record_list_temp:
        field.store_record()
    length = int(len(product_record_list_temp))
    product_record_list_temp = []
    if length != 0:
        counter = 0
        return render_template("ADDPRODUCT.html", product=product_record_list_temp, counter=counter)
    return render_template("ADDPRODUCT.html")


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


@ app.route("/VIEWALL")
def vieall():
    temp = []
    display = []
    myfile = open("PRODUCT.txt", "r")
    temp = myfile.read().splitlines()
    myfile.close
    for field in temp:
        produt_id_temp = get_field(field, 1)
        product_name = get_field(field, 2)
        product_sale_price = get_field(field, 3)
        product_purchase_price = get_field(field, 4)
        product_stock_temp = get_field(field, 5)
        record = Product(produt_id_temp, product_name,
                         product_sale_price, product_purchase_price, product_stock_temp)
        display.append(record)
    print(product_record_list_temp)

    return render_template("VIEWALL.html", product=display)


def read_data():
    global product_record_list_per
    myfile = open("PRODUCT.txt", "r")
    product_record_list_per = myfile.read().splitlines()
    myfile.close


@app.route("/store_data", methods=['POST', 'GET'])
def stock():
    global product_record_list_per
    global product_record_list_temp
    produt_id = request.form['id']
    product_stock = request.form['quantity']
    read_data()
    counter = 0
    idx = 0
    for field in product_record_list_per:
        produt_id_temp = get_field(field, 1)
        product_name = get_field(field, 2)
        product_sale_price = get_field(field, 3)
        product_purchase_price = get_field(field, 4)
        product_stock_temp = get_field(field, 5)
        if(produt_id == produt_id_temp):
            idx = counter
            temp = produt_id+","+product_name+","+product_sale_price + \
                ","+product_purchase_price+","+product_stock+","

        counter = counter+1

    product_record_list_per[idx] = temp
    myfile = open("PRODUCT.txt", "w")
    for field in product_record_list_per:
        print(field, file=myfile, sep="\n")
    myfile.close()
    print("DATA IS UPDATED ")

    return render_template("STORE.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
