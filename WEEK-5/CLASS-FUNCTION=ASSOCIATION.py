class Product:
    _id = -1
    name = ""
    price = 0

    def __init__(self, _id, name, price):
        self._id = _id
        self.name = name
        self.price = price

    def get_discount(self, percentage):
        discount = self.price * percentage / 100
        return discount


class Customer:
    _id = -1
    name = ""
    list_products = []

    def __init__(self, cid, cname):
        self._id = cid
        self.name = cname

    def buy_product(self, product):
        self.list_products.append(product)

    def display_all_product(self):
        for product in self.list_products:
            print(product.name, "   ", product.price)


p1 = Product(1, "Product 1", 5000)
p2 = Product(2, "Product 2", 658)
p3 = Product(3, "Product 3", 152)

customer1 = Customer(1, "Tajamal")
customer1.buy_product(p1)
customer1.buy_product(p2)
customer1.buy_product(p3)


print(customer1.name)
customer1.display_all_product()
