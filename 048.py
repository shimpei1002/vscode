N,K=map(int,input().split())
A,B=[],[]
C=[]
sum=0
for _ in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(a-b)
D=B+C
D.sort(reverse=True)
for i in range(K):
    sum+=D[i]
print(str(sum))