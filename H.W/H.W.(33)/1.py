class Animal:
    def __init__(self,species):
        self.species=species
    def show_species(self):
        print(f"I'm an -{self.species}")
    def make_sound(self):
        print("Grrr!")
class Dog(Animal):
    def __init__(self):
        self.species="dog"
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def __init__(self):
        self.species="cat"
    def make_sound(self):
        print("Meow!")
def show_animal_info(animal):
    if animal.species=="ordinary animal" or animal.species=="dog" or animal.species=="cat" or animal.species=="animal":
        animal.show_species()
        animal.make_sound()
    else:
        print(f"{animal.species.title()} this is not an animal")
a1=Animal("ordinary animal")
animal=show_animal_info(a1)
a2=Dog()
animal=show_animal_info(a2)
a3=Cat()
animal=show_animal_info(a3)
a4=Animal("book")
animal=show_animal_info(a4)
a5=Animal(str(input("Введите вид животного:")))
animal=show_animal_info(a5)
