#                                       810
print(810)
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def square(self):
        print(f"Square: {self.a*self.b}")
r1=Rectangle(2,3)
r1.square()
#                                       812
print("")
print(812)
class Line:
    def __init__(self,line):
        self.line=line
    def give(self):
        print(self.line.upper())
line=str(input("Введите рядок:"))
l1=Line(line)
l1.give()
#                                       813
print("")
print(813)
from Shop import Shop
class Discount(Shop):
    def __init__(self,shop_name,store_type,discount_products,number_of_units=0):
        Shop.__init__(self,shop_name,store_type,number_of_units=0)
        self.discount_products=discount_products
    def get_discounts_products(self):
        for i in self.discount_products:
            print(i)
s1=Shop("Store","game")
print(s1.shop_name)
print(s1.store_type)
s1.describe_shop()
s1.open_shop()
s2=Shop("Shop","electronic")
s2.describe_shop()
print(f"Товарів:{s1.number_of_units} типів")
s1.number_of_units=5
print(f"Товарів:{s1.number_of_units} типів")
s1.set_number_of_units()
print(f"Товарів:{s1.number_of_units} типів")
a=int(input("Введіть на скільки збілюшується кількість видів товару:"))
s1.increment_number_of_units(a)
print(f"Товарів:{s1.number_of_units} типів")
store_discount=Discount("Store_d","food",["apples","carrots","potatoes"])
store_discount.get_discounts_products()
all_store=Shop("A_shop","animal")
all_store.describe_shop()
