N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
sum=0
a,b,c=[0]*46,[0]*46,[0]*46
for i in range(N):
    tmp=A[i]%46
    a[tmp]+=1
    tmp=B[i]%46
    b[tmp]+=1
    tmp=C[i]%46
    c[tmp]+=1

for i in range(46):
    for j in range(46):
        for k in range(46):
            if((i+j+k)%46==0):
                sum+=a[i]*b[j]*c[k]
print(str(sum))
        
