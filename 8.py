#def fullname (name,surname):
    #print(f"{name.title()} {surname.title()}")
    #a=f"{name.title()} {surname.title()}"
    #return a

#while True:
    #print("Введиет имя и фамилию")
    #name=input("Имя:")
    #surname=input("Фамилия")
    #print(f"{name.title()} {surname.title()}")
    #fullname(name,surname)
    #b=fullname(name,surname)
    #print(b)
spisok_model= ["Машина","Робот","Айфон","Чехол"]
spisok_usera=[]
def pechat(a,b):
    while spisok_model:
        raspec=a.pop()
        b.append(raspec)
        print(spisok_usera)
def gotovo(b):
    for i in b:
        print(i)
pechat(spisok_model,spisok_usera)
gotovo(spisok_usera)
