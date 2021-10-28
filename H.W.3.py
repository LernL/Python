#3.4
print(3.4)
my_list= ["Ilya", "Bogdan", "Artem"]
print("Hello," + my_list[0] + ",I invite you to dinner.") 
print("Hello," + my_list[1] + ",I invite you to dinner.")
print("Hello," + my_list[2] + ",I invite you to dinner.")
#3.5
print()
print(3.5)
print(my_list[2] +" will not be able to come")
my_list[2]="Danya"
print(my_list[0] + ",I hope you will come?")
print(my_list[1] + ",have you changed your mind about coming to me yet?")
print(my_list[2] + ",I invite you to dinner, will you come?")
#3.6
print()
print(3.6)
print("Expanded table ")
my_list.insert(-4,"Vlad")
my_list.insert(-2,"Egor")
my_list.append("Oleg")
print(my_list[0] + ",the invitation is still valid.")
print(my_list[1] + ",the invitation is still valid.")
print(my_list[2] + ",the invitation is still valid.")
print(my_list[3] + ",the invitation is still valid.")
print(my_list[4] + ",the invitation is still valid.")
print(my_list[5] + ",the invitation is still valid.")
#3.7
print()
print(3.7)
print("Only two people are invited to dinner")
print(my_list[5] + ",sorry, but due to sudden changes of plans, I cannot accept you. ")
my_list.pop()
print(my_list[4] + ",sorry, but due to sudden changes of plans, I cannot accept you. ")
my_list.pop()
print(my_list[3] + ",sorry, but due to sudden changes of plans, I cannot accept you. ")
my_list.pop()
print(my_list[2] + ",sorry, but due to sudden changes of plans, I cannot accept you. ")
my_list.pop()
print(my_list[0] + ",the invitation is valid.")
print(my_list[1] + ",the invitation is valid.")
#3.9
print(3.9)
print(str(len(my_list)) + " people")
del my_list[1]
del my_list[0]
print(my_list)
#3.8
print()
print(3.8)
country= ["Poland", "Britian", "USA", "German", "Spain"]
print(country)
print(sorted(country))
print(country)
a = sorted(country, reverse = True)
print(a)
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort()
print(country)
import os
os.system('pause')

