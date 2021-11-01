#                                       8.3
#def make_shirt(text,r):
#    a=f'Текст:"{text.title()}", размер:{r}'
#    return a
#text=str(input("Введите текст на футболке: "))
#r=int(input("Введите размер футболки: "))
#b=make_shirt(text,r)
#print(b)
#                                       8.4
#def make_shirt(text,r):
#    print(f'Текст:"I love Python", размер:L')
#    a=f'Текст:"{text.title()}", размер:{r}'
#    return a
#text=str(input("Введите текст на футболке: "))
#r=int(input("Введите размер футболки: "))
#b=make_shirt(text,r)
#print(b)
#                                       8.5
#def describe_city(city,country):
#    a=f'{city.title()} is in {country.title()}'
#    return a
#i=0
#while i<3:
#    i+=1
#    print("Если вы хотите закончить, напишите 'break'")
#    city = input("Введите город: ")
#    if city =="Kiev" or city =="Dnepr":
#        country = 'Ukraine'
#    elif city=="break":
#        break
#    else:
#        country=input("Введите страну: ")
#    b=describe_city(city,country)
#    print(b)
#                                       8.6
#def city_country(city,country):
#    a= f' {city.title()}, {country.title()}'
#    return a
#i=0
#while i<3:
#    i+=1
#    print("Если вы хотите закончить, напишите 'break'")
#    city = input("Введите город: ")
#    if city=="break": 
#        break
#    else:
#        country=input("Введите страну: ")
#        b=city_country(city,country)
#        print(b)
#                                           8.7;8.8
#def make_album(name_s,name_a,signs):
#    if signs==None:
#        a = f'{name_s.title()} \n{name_a.title()}'
#    else:
#        a = f'{name_s.title()} \n{name_a.title()} \n{signs} signs'
#    return a
#i=0
#while i<3:
#    i+=1
#    print("Если вы хотите закончить, напишите 'break'")
#    name_s=str(input("Введите имя исполнителя: "))
#    if name_s=="break":
#        break
#    name_a=str(input("Введите название альбома: "))
#    signs=str(input("Введите количество дороже(Если не известно, нажмите 'Enter'"))
#    if signs =="":
#        signs=None
#    b=make_album(name_s,name_a,signs)
#    print(b)
#                                           8.12
def sandwich(a,b):
    b+=a
    return b
s=""
b=""
x=" "
while True:
    a=str(input("Введите компонент вашего сэндвича (Если вы закончили, напишите 'Ready'): "))
    if a=="Ready":
        break
    else:
        s+=sandwich(a,b)+x

print(s)
