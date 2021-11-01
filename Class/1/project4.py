a=int(input("Введите перове число: "))
b=int(input("Введите второе число: "))
if a>b:
    a=1
    b=0
    print(f"a={a}, b={b}")
elif a<b:
    a=0
    b=1
    print(f"a={a}, b={b}")
else:
    print("Они равны")
