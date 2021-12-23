def funct(p1):
    if p1==i:
        return True
    else:
        return False
p1=["Python","C++","C#"]
p2=["HTML","Python","C#","JS"]
for i in p2:
    t=list(filter(funct,p1))
    if t==[]:
        continue
    else:
        print(t)
