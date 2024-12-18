N=int(input())
C=[]
P=[]
for _ in range(N):
    c,p=list(map(int,input().split())) 
    C.append(c)
    P.append(p)
Q=int(input())
L=[]
R=[]
for _ in range(Q):
    l,r=list(map(int,input().split())) 
    L.append(l)
    R.append(r)
sum1,sum2=[],[]
sum1.append(0)
sum2.append(0)
for j in range(N):
    if(C[j]==1):
        sum2.append(sum2[-1])
        sum1.append(sum1[-1]+P[j])
    else:
        sum1.append(sum1[-1])
        sum2.append(sum2[-1]+P[j])
for i in range(Q):
    print(str(sum1[R[i]]-sum1[L[i]-1])+' '+str(sum2[R[i]]-sum2[L[i]-1]))