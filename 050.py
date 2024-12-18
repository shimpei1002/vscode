import math
sum=0
N,L=map(int,input().split())
for i in range(N//L+1):
    r=N-L*(i)
    sum+=math.comb(r+i,r)
sum=sum%(10**9+7)
print(str(sum))