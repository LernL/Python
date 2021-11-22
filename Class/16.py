#def month(m):
#    season=f"Error!"
#    for i,j in month_seasons.items():
#       if m in i:
#            season=j
#        elif m>12 and m<0:
#            season=f"Error!"
#        return season
#month_seasons={
#    (12,1,2):"Zima",
#    (3,4,5):"Vesna",
#    (6,7,8):"Leto",
#    (9,10,11):"Osen"
#}
#m=int(input("Enter number if month"))
#a=month(m)
#print(a)

#num = [1,2,3,4,5]
#num2 = [a**2 for a in num if a>4]
#print(num2)
#for i in num:
#    num2.append(i)
#print(num2)

import random

num=[random.random() for a in range(15)]
print(num)
