#auto=("Ferrari","Maz","zigul","kin","lamborgini",25,78)
#print(auto)
#print(auto[0:2])
#print(auto[-1])
#print(auto[-2])
#print(f'{auto[2]}={auto.index("zigul")}')

#num=(132,10,15,45,10,10,16)
#a=num.count(10)
#print(a)
#b=sum(num)
#print(b)
#c=min(num)
#print(c)
#d=max(num)
#print(d)

#dictName={'Illia':18, 'Maksym':20, 'Den': 24, 'Roma':7}
#print(dictName['Maksym'])
#print(dictName.values())
#for i,j in dictName.items():
#    print(f"{i} age - {j}")

dictName={'Illia':18, 'Maksym':20, 'Den': 24, 'Roma':7}
dictAuto={'Kia_KS': 2014, 'Toyota_Supra': 2000, 'BMW_M2': 2016, 'Volkswagen-Tiguan':2020}
dictMixed = dictName.copy()
dictMixed.update(dictAuto)
#dictMixed=dictName | dictAuto
#dictName |=dictAuto
print(dictMixed)
a=dictName.get('Artem','user_not_found')
dictAuto.clear()
print(a)
print(dictAuto)
