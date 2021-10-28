import math
a=int(input("a= "))
if a<0:
    print("Нульова порожнина")
elif a>0:
    x = math.sqrt(a)
    print(f"x={x} or x={-x}")
else:
    print(0)
