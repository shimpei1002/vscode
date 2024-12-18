N,Q=map(int,input().split())
answer=0
A=list(map(int,input().split()))
B=[]
for i in range(N-1):
    B.append(A[i]-A[i+1])
    answer+=abs(B[i])
for _ in range(Q):
    l,r,v=map(int,input().split())
    if(l!=1):
        tmp=B[l-2]
        B[l-2]-=v
        answer+=abs(B[l-2])-abs(tmp)
    if(r!=N):
        tmp=B[r-1]
        B[r-1]+=v
        answer+=abs(B[r-1])-abs(tmp)
    print(str(answer))