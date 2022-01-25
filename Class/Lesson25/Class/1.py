#class Human:
#    pass
#p1=Human()
#p1.name="Den"
#p1.surname="Dmitriev"
#p1.place_of_birth="UA"
#p2=Human()
#p2.name="Alexey"
#p2.surname="Kosenko"
#p2.place_of_birth="UA"
#print(f"Name: {p2.name}, surname: {p2.surname}, place of birth: {p2.place_of_birth}")
#print(f"Name: {p1.name}, surname: {p1.surname}, place of birth: {p1.place_of_birth}")
class Human:
    def info(self,n):
        for i in range(n):
            print(f"Name: {self.name}, surname: {self.surname}, place of birth: {self.place_of_birth}")
    def year(self,year_new):
        return year_new-self.year_of_birth
p1=Human()
p1.name="Den"
p1.surname="Dmitriev"
p1.place_of_birth="UA"
p1.year_of_birth=1997
p1.info(7)
print(p1.year(2021))
p2=Human()
p2.name="Alexey"
p2.surname="Kosenko"
p2.place_of_birth="UA"
p2.year_of_birth=2007
p2.info(5)
print(p2.year(2021))
p3=Human()
p3.name="Roman"
p3.surname="Osinniy"
p3.place_of_birth="UA"
p3.year_of_birth=2005
p3.info(10)
print(p3.year(2021))
