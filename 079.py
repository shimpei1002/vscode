H,W=map(int,input().split())
A,B=[],[]
sum=0

for _ in range(H):
    a=list(map(int,input().split()))
    A.append(a)
for _ in range(H):
    b=list(map(int,input().split()))
    B.append(b)
for i in range(W-1):
    for j in range(H-1):
        tmp=B[i][j]-A[i][j]
        A[i][j]+=tmp
        A[i][j+1]+=tmp
        A[i+1][j]+=tmp
        A[i+1][j+1]+=tmp
        sum+=abs(tmp)

if(A==B):
    print('Yes')
    print(str(sum))
else:
    print('No')