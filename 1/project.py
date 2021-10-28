a=int(input("Введите вклад"))
p=float(input("Введите %"))
m=int(input("Введите месяц"))
if m>12:
    s=a+a*(p/100)
    print(s)
else:
    print(a)
    
