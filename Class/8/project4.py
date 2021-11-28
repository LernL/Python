t=[2.3,4.5,3.5,10.3,5]
a=0
b=t[0]
for i in t:
    a=a+i
    if i>b:
        b=i
print(a)
print(b)
