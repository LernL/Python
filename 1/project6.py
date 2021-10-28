import math
a=float(input("Введите радиус: "))
b=float(input("Введите сторону: "))
if a== int((b*math.sqrt(3))/6):
    print("Можно")
else:
    print("Не можно")
