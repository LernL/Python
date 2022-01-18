class Shop:
    def __init__(self,shop_name,store_type,number_of_units=0):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=number_of_units
    def describe_shop(self):
        print(f"'{self.shop_name.title()}' have {self.store_type} type")
    def open_shop(self):
        print("Online-shop open!")
    def set_number_of_units(self):
        self.number_of_units=int(input("Введіть кількість товару:"))
    def increment_number_of_units(self,a):
        self.number_of_units+=a
        return  self.number_of_units
