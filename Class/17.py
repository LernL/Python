#a=[]
#for i in range(10):
#    a.append(i)
#print(a)

#a=[i for i in range(10) if i>7 if i%2==0]
#print(a)
#a=[i if i>4 else "false" for i in range(10) ]
#print(a)
#a=["true_2" if i%2==0 else "true_3" if i%3==0  else "false" for i in range(1,11) ]
#print(a)

#a=[1,2,3]
#b=[4,5,6,7]
#c=[(i,g) for i in a for g in b]
#print(c)
#for f in c:
#    print(f)

#case_1 = ["key1", "key2", "key3"]
#case_2 = ["value_1", "value_2", "value_3"]
#c = {i:g for i in case_1 for g in case_2}
#print(c)
#for f,l in c.items():
#    print(f,l)

c = {i:i**2 for i in range(20) if i>=5}
m = {g:l for g,l in c.items() if l<=100}
j = {key:("true_2" if val%2==0 else key**2) for key,val in m.items()}
for k,v in j.items():
     print(k,v)
