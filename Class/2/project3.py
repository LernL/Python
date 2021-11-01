a=float(input("Какой вклад?"))
b=float(input("Какой %?"))
g=0
for g in range (5):
    g+=g
    a=a+a*(b/100)
    print(a)
