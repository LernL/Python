a=float(input("Число:"))
if a<10 and a>2:
    for i in  range(10):
        i+=1
        c=a*i
        print(f"{a} * {i} = {c}")
else:
    print("Введите число от 2 до 9")
