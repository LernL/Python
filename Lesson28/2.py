class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def info(self):
        print(f"{self.name} says hello!")
class Student(Human):
    def __init__(self,name,age,place_of_studying):
        Human.__init__(self,name,age)
        self.place_of_studying=place_of_studying
    def study(self):
        print(f"Student {self.name} studies")
    def info(self):
        print(f"Student created, name:{self.name}, age:{self.age}")
    def studying(self):
        print(f"{self.place_of_studying}")
class Teacher(Human):
    def teach(self):
        print(f"{self.name}-teacher")
s1=Student("Roma",16,"KPL")
t1=Teacher("Mikola",45)
s1.info()
s1.studying()
