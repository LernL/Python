import random
n=3
m=3
mat=[[random.randint(1,10) for j in range(m)] for i in range(n)]
for l in mat:
    print(f"\t{l}")
for j in range(m):
    for i in range(n):
        if i==j:
            a=mat[i][j]
            print(a)
