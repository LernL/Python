class Mashin:
    def __init__(self,name,company,place_of_creat,year_of_creat):
        self.name=name
        self.company=company
        self.place_of_creat=place_of_creat
        self.year_of_creat=year_of_creat
    def info(self):
        print(f"Name: {self.name}, company: {self.company}, place of creat: {self.place_of_creat}")
    def year(self,year_new):
        return year_new-self.year_of_creat
m1=Mashin("Volkswagen Scirocco","Karmann","Germany",1974)
m1.info()
print(m1.year(2021))
m2=Mashin("KrAZ-256B1","KrAZ" ,"UA",1966)
m2.info()
print(m2.year(2021))
m3=Mashin("Lamborghini Gallardo","Lamborghini","Italy",2003)
m3.info()
print(m3.year(2021))
m4=Mashin("Benz Velo","	Rheinische Gasmotorenfabrik Benz & Cie.","Germany",1894)
m4.info()
print(m4.year(2021))
m5=Mashin("Ford Model T","Ford Motor Company","USA",1908)
m5.info()
print(m5.year(2021))
m6=Mashin("Lamborghini 350 GT","Automobili Lamborghini S.p.A","Italy",1964)
m6.info()
print(m6.year(2021))
