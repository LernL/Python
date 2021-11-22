#                                               6.1
print("6.1")
data={
    "first_name":"Tima",
    "last_name":"Pylypenko",
    "age":16,
    "city":"Krivoy Rog"
    }
for i,n in data.items():
    print(f"{i}: {n}")
#                                               6.2
print("")
print("6.2")
numbers={
    "Ilya":15,
    "Roma":38,
    "Artem": 47,
    "Bogdan": 60,
    "Danya": 90
    }
for i,n in numbers.items():
    print(f"{i}: {n}")
#                                               6.3+6.4
print("")
print("6.3+6.4")
dict={
    "Git":"Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.",
    "Terminal":"A terminal emulator, terminal application, or term,is a computer program that emulates a video terminal within some other display architecture",
    "If":"The if-elif-else conditional statement (sometimes called the branching statement) is the main selection tool in Python.",
    "While":"While is one of the most versatile loops in Python, and is therefore quite slow. Executes the body of the loop as long as the loop condition is true.",
    "Continue":"The continue statement starts the next pass of the loop, bypassing the rest of the loop body (for or while)",
    "Break":"The break statement terminates the loop early.",
    "Else":"The word else, used in a for or while loop, checks whether the loop was exited with a break statement, or in a 'natural' way. The block of statements inside the else will be executed only if the loop was exited without the help of break.",
    "Dict":"Python dictionaries are unordered collections of arbitrary key-accessed objects. They are sometimes also called associative arrays or hash tables.",
    "Function":"A function is a block of code which only runs when it is called."
    }
for i,n in dict.items():
    print(f"{i}: \n{n}")
#                                               6.5
print("")
print("6.5")
data={
    "Nile":"Egypt",
    "Dnipro":"Ukraine",
    "Missouri":"USA",
    "Loir":"France",
    "Thames":"English"
    }
for i,n in data.items():
    print(f"{i}:{n}")
print("")
for i in data.keys():
    print(i)
print("")
for n in data.values():
    print(n)
#                                               6.7
print("")
print("6.7")
people={
    "user_0":{
        "first_name":"Tima",
        "last_name":"Pylypenko",
        "age":16,
        "city":"Krivoy Rog"
        },
    "user_1":{
        "first_name":"Ilia",
        "last_name":"Yushenko",
        "age":16,
        "city":"Krivoy Rog"
        },
    "user_2":{
        "first_name":"Artem",
        "last_name":"Dorogin",
        "age":1,
        "city":"Krivoy Rog"
        }
        
    }
for i,n in people.items():
    print(f"\n{i}:")
    for a,b in n.items():
        print(f"{a}:{b}")
#                                               6.8
print("")
print("6.8")
pets={
    "animal_0":{
        "nickname":"Lord",
        "owner":"Tima",
        "type":"dog",
        },
    "animal_1":{
        "nickname":"Ceaser",
        "owner":"Ilia",
        "type":"turtle",
        },
    "user_2":{
        "nickname":"Masha",
        "owner":"Ilia",
        "type":"turtle",
        }
        
    }
for i,n in pets.items():
    print(f"\n{i}:")
    for a,b in n.items():
        print(f"{a}:{b}")
#                                               6.9
print("")
print("6.9")
favourite_places={
    "Ilia":"ATB",
    "Artem":("Francua","ATB"),
    "Danya":("Empire of sport","Francua","ATB")
    }
for i,n in favourite_places.items():
    print(f"{i}:{n}")
#                                               6.10
print("")
print("6.10")
numbers={
    "Ilya":(15,32,99),
    "Roma":(38,314,51325),
    "Artem": (47,214,591),
    "Bogdan": (60,2,9191),
    "Danya": (90,9,6701)
    }
for i,n in numbers.items():
    print(f"{i}: {n}")
#                                                   6.11
print("")
print("6.11")
cities={
    "Kiev":{
        "Country":"Ukraine;",
        "Population":"2 951 952 people;",
        "Fact":"Monument to Bohdan Khmelnitsky. The cliff on which the monument to Bohdan Khmelnitsky stands is made of the remains of stones that were used to build the Nikolaev chain bridge (blown up by the retreating Red Army in 1941).",
        },
    "London":{
        "Country":"England;",
        "Population":"8 961 989 people;",
        "Fact":"The exact age of London is unknown, but, judging by the found chronicles, it is about two thousand years old.",
        },
    "Berlin":{
        "Country":"German;",
        "Population":"3 644 826 people;",
        "Fact":"The first traffic light in Europe was installed in Berlin in 1924. A copy can still be seen at Potsdamer Platz today.",
        }
        
    }
for i,n in cities.items():
    print(f"\n{i}:")
    for a,b in n.items():
        print(f"{a}:{b}")
