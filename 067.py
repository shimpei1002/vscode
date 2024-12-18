N,K=map(int,input().split())
ans=0
iter=0
sum=0
N=str(N)
for _ in range(K):
    for i in range(len(str(N))-1,-1,-1):
        ans+=int(N[i])*(8**iter)
        iter+=1
    iter=0
    while(ans!=0):
        if(ans%9!=8):            
            sum+=(ans%9)*(10**iter)
        else:
            sum+=5*(10**iter)
        ans=ans//9
        iter+=1
    x=sum
    ans=0
    iter=0
    sum=0
    N=str(x)
print(str(x))