class Shop:
    def __init__(self,shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(f"{self.shop_name.title()} has {self.store_type} type; \nNumber of units:{self.number_of_units}")
    def open_shop(self):
        print(f"{self.shop_name.title()} open!")
    def set_number_of_units(self,new_number_of_units):
        self.number_of_units=new_number_of_units
        print(f"New number of units:{self.number_of_units}")
    def increment_number_of_units(self,a):
        self.number_of_units+=a
        print(f"New number of units:{self.number_of_units}")
class Discount(Shop):
    def __init__(self,shop_name,store_type):
        Shop.__init__(self,shop_name,store_type)
        self.discount_products=["Iphone","Apple watch","IMac"]
    def get_discount_products(self):
        for i in self.discount_products:
            print(f"On this products discount!:{i}")
