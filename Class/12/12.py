def pizza(size, *type):
    print(f"Вы заказали такие пиццы с размером {size}: {type}")
    for i in type:
        print(f'-{i}')

size=input("Размер: ")
pizza(size,"4cheese")
pizza(size,"diablo","gavaiskaya","4meat","peperoni","ukrainskaya")
pizza(size,"4cgeese","4meat")
