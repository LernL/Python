class Animal:
    def __init__(self,name,age,place_of_live,year_of_birth):
        self.name=name
        self.age=age
        self.place_of_live=place_of_live
        self.year_of_birth=year_of_birth
    def info(self):
        print(f"Name: {self.name}, age: {self.age}, place of live: {self.place_of_live}")
    def year(self,year_new):
        return year_new-self.year_of_birth
a1=Animal("Lord",10,"UA",2011)
a1.info()
print(a1.year(2021))
a2=Animal("Petr",2 ,"UA",2019)
a2.info()
print(a2.year(2021))
a3=Animal("Simka",7,"UA",2014)
a3.info()
print(a3.year(2021))
a4=Animal("Karl",5,"UA",2016)
a4.info()
print(a4.year(2021))
a5=Animal("Rond",3,"UA",2018)
a5.info()
print(a5.year(2021))
