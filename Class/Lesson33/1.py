from Shop import *
new_number_of_units=int(input("Number of units:"))
s1=Shop("Rozetka","electronical")
s1.describe_shop()
s1.open_shop()
s2=Shop("ATB","Food")
s2.describe_shop()
s2.set_number_of_units(new_number_of_units)
s2.increment_number_of_units(int(input("Enter value on +:")))
s3=Discount("Iphone","Ipad",)
s3.get_discount_products()
                
        
