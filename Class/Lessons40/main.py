from math import *
# 1
def name():
    name = str(input("Enter name:"))
    print(f"Hi,{name.title()}")


#name()


# 2
def string():
    string = str(input("Write string:"))
    n = int(input("Write n:"))
    while n:
        print(string)
        n -= 1


#string()


# 6
def max1():
    numb1 = int(input("Write number1:"))
    numb2 = int(input("Write number2:"))
    if numb1 < numb2:
        print(f"{numb2}>{numb1}\n{numb2}")
    elif numb1 > numb2:
        print(f"{numb1}>{numb2}\n{numb1}")
    else:
        print("equal")


#max1()


# 7
def max2():
    numb1 = int(input("Write number1:"))
    numb2 = int(input("Write number2:"))
    numb3 = int(input("Write number3:"))
    print(max(numb1, numb2, numb3))


#max2()


# 8
def triangle():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print("This triangle can be")
    else:
        print("This triangle can't be")


#triangle()


# 9
def merge():
    word1 = str(input("Write 1 word:"))
    word2 = str(input("Write 2 word:"))
    result = word1 + ' ' + word2
    print(result)


#merge()


# 10
def calcul():
    numb1 = float(input("Write 1 number:"))
    numb2 = float(input("Write 2 number:"))
    operation = str(input("Write operation:"))
    if operation == "+":
        print(numb1 + numb2)
    elif operation == "-":
        print(numb1 - numb2)
    elif operation == "*":
        print(numb1 * numb2)
    elif operation == "/":
        print(numb1 / numb2)
    else:
        print("Unknow operation")


#calcul()


# 11
def HTML():
    teg = str(input("Write name teg:"))
    string = str(input("String:"))
    print(f"<{teg}>{string}</{teg}>")


#HTML()


# 12
def seasons():
    number = int(input("Write number:"))
    if number == 12 or number == 1 or number == 2:
        print("Winter")
    elif number == 3 or number == 4 or number == 5:
        print("Spring")
    elif number == 6 or number == 7 or number == 8:
        print("Summer")
    elif number == 9 or number == 10 or number == 11:
        print("Autumn")
    else:
        print("Wrong number")


#seasons()


# 13
def gistograms(a):
    for i in a:
        print('*' * i)


#gistograms([2, 7, 1, 4, 2, 3, 9, 3])


# 14
def parity():
    number = float(input("Write number:"))
    if number % 2 == 0:
        print(f"{number}/2")
    else:
        print(f"{number} isn't /2")


#parity()


# 15
#def list():
#    numbers = str(input(("Write numbers:")))
#    list=[int(i) for i in numbers.split()]
#    print(list[0:2])
#list()
#16
def factorial():
    b=1
    number=int(input("Write number:"))
    for i in range(1,number+1):
        b=b*i
    print(b)
factorial()
#17
def S_triangle():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    if (a + b) > c and (b + c) > a and (a + c) > b:
        S = sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - 1) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))
        print(S)
    else:
        print("This triangle can't be")
def rectanle():
    a = int(input("a:"))
    b = int(input("b:"))
    S=a*b
    print(S)
def circle():
    r = int(input("r:"))
    S=pi*r**2
    print(S)
def question():
    quest=str(input("What figure do you want to know the area:"))
    if quest=="rectangle":
        rectanle()
    elif quest=="circle":
        circle()
    elif quest=="triangle":
        S_triangle()
    else:
        print("I can't identify this figure")
question()