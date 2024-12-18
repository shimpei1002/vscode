import math
A,B=map(int,input().split())
x=math.lcm(A,B)
if(x>10**18):
    print('Large')
else:
    print(str(x))