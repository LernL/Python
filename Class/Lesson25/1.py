def f(x):
    if x%2==0:
        return True
    else:
        return False
import random
n=int(input("n="))
arr=[random.randint(0,10) for a in range(n)]
t=list(filter(f,arr))
print(t)
