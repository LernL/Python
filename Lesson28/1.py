class Human:
    def __init__(self,name,surname,place_of_birth,year_of_birth):
        self.name=name
        self.surname=surname
        self.place_of_birth=place_of_birth
        self.year_of_birth=year_of_birth
    def info(self,n):
        for i in range(n):
            print(f"Name:{self.name},\n Surname:{self.surname},\n Place:{self.place_of_birth},\n Year:{self.year_of_birth}")
    def age(self,year):
        return year-self.year_of_birth
p1=Human('Den','Dmitriev','UA',1997)
p1.info(1)
b=p1.age(2022)
print(b)
