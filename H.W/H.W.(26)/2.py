class Human:
    def __init__(self,name,surname,age,place_of_birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_birth=place_of_birth
    def info(self):
        print(f"Name:'{self.name}\nSurname:'{self.surname}'\nAge:'{self.age}'\nPlace:'{self.place_of_birth}'")
name=input("Привет.Чтобы продолжить, введите ваше имя:")
surname=input("Записал.А теперь фамилию:")
age=input("Так.А теперь возраст:")
place=input("И последний пункт.Откуда ты?")
print("Вот твои данные:")
p1=Human(name,surname,age,place)
p1.info()
