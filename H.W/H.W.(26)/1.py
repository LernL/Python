import math
class Triangle:
    def s(self,a,b,c):
        print(f"s={math.sqrt(((a+b+c)/2)*((((a+b+c)/2)-a)*(((a+b+c)/2))-b)*(((a+b+c)/2)-c))}")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
t1=Triangle()
t1.s(a,b,c)
