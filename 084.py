import math
N=int(input())
S=str(input())
x=1
max=math.comb(N,2)
for i in range(N-1):
    if(S[i]==S[i+1]):
        x+=1
    else:
        if(x!=1):
            max-=math.comb(x,2)
            x=1
        else:
            x=1
if(x!=1):
    max-=math.comb(x,2)
    x=2
print(str(max))