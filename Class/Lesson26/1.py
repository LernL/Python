import math
x=float(input("x="))
y=float(input("y="))
#if x>(-math.pi) and x<math.pi/4:
#    print(f'y={(-math.cos(x-math.pi))**2}')
#elif x>=math.pi/4 and x<=1:
#    print(f'y={math.sqrt(abs(x+1))}')
#elif x>1:
#    print(f"y={1/(x-1)}")
#else:
#    print("Error")
if abs(x*y)<1 and x<0:
    print(f"z={(x+y)/math.pow(math.e,x*y)}")
elif x>2 and y<=0:
    print(f"z={}")
