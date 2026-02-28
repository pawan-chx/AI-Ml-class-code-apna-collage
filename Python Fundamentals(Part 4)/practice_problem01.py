        #=> DEGINE AND CREAT AN ONLINE STORE FOR PRODUCTS (NAME, PRICE)

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name 
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}") 

    @classmethod
    def get_count(cls):
        print(f"total product in store = {cls.count}")  

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount*price/100)
        print(f"discounted price = {final_price}")    

product1 = Product("mouse", 600) 
product2 = Product("keyboard", 800)
product3 = Product("laptop", 900)   

product1.get_info()
Product.get_count()
product1.calc_discount(product1.price, 12)