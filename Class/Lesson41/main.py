#1
from math import *
r=float(input("r="))
s=pi*r**2
print(s)
#2
Password=str(input("Write password:"))
print("Password created!")
while True:
    Check_passw=str(input("Enter password"))
    if Password==Check_passw:
        print("The password is correct!")
        break
    else:
        print("Try again!")
#3
age=float(input("Enter your age:"))
if age<23 and age>0:
    print("You can't take credit.")
elif age>23:
    print("You can tae credit.")
else:
    print("Incorrect age.")
#4
mark=int(input("Write your mark:"))
if mark>10:
    print("Good mark.")
elif mark<9 and mark>7:
    print("Normal mark.")
elif mark<6 and mark>4:
    print("Bad mark")
elif mark<3 and mark>1:
    print("Very bad mark")
else:
    print("Incorrect mark")
#5
x=float(input("x="))
y=float(input("y="))
if x>y:
    z=sqrt(x*y)
    print(z)
else:
    z=log1p(x*y)
    print(z)
#6
temp=float(input("Enter temperature:"))
if temp>20:
    print("on")
else:
    print("off")
#7
n=int(input("Enter number:"))
if n%2==0:
    print("He's second.")
elif n%2==1 and n==0:
    print("He's first.")
else:
    print("Incorrect number")
#8
a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
if a+b>c and a+c>b:
    print("This rectangle can be")
    if a==b or a==c or b==c:
        print("This is an isosceles triangle")
    elif a==b and a==c:
        print("This is an equilateral triangle")
    else:
        print("This is a scaled triangle")
else:
    print("This rectangle can't be")
#9
x=float(input("x="))
y=float(input("y="))
while True:
    if x>0 and y>0:
        print("First quarter")
        break
    elif x<0 and y>0:
        print("Second quarter")
        break
    elif x<0 and y<0:
        print("Third quarter")
        break
    elif x>0 and y<0:
        print("Fourth quarter")
        break
    elif x==0:
        print("Incorrect x")
        x = float(input("x="))
    elif y==0:
        print("Incorrect y")
        y = float(input("y="))
#10
x=float(input("x="))
if x>0:
    y=2*x-10
elif x==0:
    y=0
else:
    y=2*abs(x)-1
print(y)
#3.1
while True:
    x=float(input('x='))
    if x<-5:
        print("Incorrect x")
    else:
        y=sqrt(x+5)
        break
print(y)
#3.2
while True:
    x=float(input('x='))
    if x==7:
        print("Incorrect x")
    else:
        y=1/(x-7)
        break
print(y)
#3.3
while True:
    x=float(input('x='))
    if x<=-5:
        print("Incorrect x")
    else:
        y=1/(sqrt(x+5))
        break
print(y)
#3.4
while True:
    x=float(input('x='))
    if x==-5:
        print("Incorrect x")
    else:
        y=1/(abs(x+5))
        break
print(y)
#3.5
while True:
    x=float(input('x='))
    if x==0:
        print("Incorrect x")
    else:
        y=1/x**7
        break
print(y)
#3.6
while True:
    x=float(input('x='))
    if x<-5 and x<7:
        print("Incorrect x")
    else:
        y=sqrt(x+5)+sqrt(x-7)
        break
print(y)
#3.7
while True:
    x=float(input('x='))
    if x<-5 and x==7:
        print("Incorrect x")
    else:
        y=sqrt(x+5)+1/(x-7)
        break
print(y)
#3.8
while True:
    x=float(input('x='))
    if x<=-5 and x==7:
        print("Incorrect x")
    else:
        y=1/(sqrt(x+5))+1/(x-7)
        break
print(y)
#4.1
x=float(input('x='))
if x>0:
    y=x
else:
    y=x**2
print(y)
#4.2
x=float(input('x='))
if x>-10 and x<5:
    y=x
else:
    y=x**2
print(y)
#4.3
x=float(input('x='))
if x>=1 and x<=5 or x>=10:
    y=x
else:
    y=x**2
print(y)
#4.4
x=float(input('x='))
if x<=0:
    y=x
elif x>0 and x<=5:
    y=x**2
else:
    y=25
print(y)