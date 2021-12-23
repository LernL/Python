class Country:
    def __init__(self,name,capital,age):
        self.name=name
        self.capital=capital
        self.age=age
    def info(self):
        print(f"Name: {self.name}, capital: {self.capital}, based: {self.age}")
    def year(self,year_new):
        return year_new-self.age
c1=Country("Italy","Rome",1861)
c1.info()
print(c1.year(2021))
c2=Country("Germany","Berlin" ,1990)
c2.info()
print(c2.year(2021))
c3=Country("France","Paris",1958)
c3.info()
print(c3.year(2021))
c4=Country("Spain","Madrid",1515)
c4.info()
print(c4.year(2021))
c5=Country("Portugal","Lissabon",1640)
c5.info()
print(c5.year(2021))
c6=Country("Greece","Athens",1821)
c6.info()
print(c6.year(2021))
c7=Country("Poland","Warsaw",1918)
c7.info()
print(c7.year(2021))
c8=Country("Luxembourg","Luxembourg",1815)
c8.info()
print(c8.year(2021))
