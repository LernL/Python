import math
class Circle:
    def len_circle(self,r):
        print(2*math.pi*r)
    def cquare_circle(self,r):
        print(math.pi*r**2)
r=float(input("R="))
c1=Circle()
c1.cquare_circle(r)
c1.len_circle(r)
c2=Circle()
c2.cquare_circle(5)
c2.len_circle(5)
c3=Circle()
c3.cquare_circle(15)
c3.len_circle(15)
c4=Circle()
c4.cquare_circle(3.14)
c4.len_circle(3.14)




