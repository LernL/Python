#n=int(input("n="))
#d=1
#while d<=n:
#    print(d**2)
#    d+=1    

#n=int(input("n="))
#s=0
#for i in range(1,n+1):
 #   s+=i
 #   i+=1
#print(s)
#r=1
#l=0
#while r<=n:
   # l+=r
   # r+=1
#print(l)

#n=int(input("n="))
#s=0
#for i in range(1,n+1,2):
   #s+=i
#print(s)
#r=1
#l=0
#while r<=n:
    #l+=r
    #r+=2
#print(l)

#k=int(input("k="))
#r=1
#l=1
#while r<=k:
    #l*=r
    #r+=1
#print(l)

#n=int(input("n="))
#k=0
#while n>0:
    #n=n//10
    #k+=1
#print(k)

n=int(input("n="))
l=0
i=1
while n>0:
    l+=(1/2**n)
    n-=1
print(l)
