class Human:
    def __init__(self,name,surname,age,place_of_birth,year_of_birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_birth=place_of_birth
        self.year_of_birth=year_of_birth
    def info(self):
        print(f"Name: {self.name}, surname: {self.surname}, place of birth: {self.place_of_birth}")
    def year(self,year_new):
        return year_new-self.year_of_birth
p1=Human("Den","Dmitriev",24,"UA",1997)
p1.info()
print(p1.year(2021))
p2=Human("Alexey","Kosenko",14,"UA",2007)
p2.info()
print(p2.year(2021))
p3=Human("Roman","Osinniy",16,"UA",2005)
p2.info()
print(p2.year(2021))
