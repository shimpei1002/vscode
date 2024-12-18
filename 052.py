N=int(input())
A= []
B=[]
result=1
for _ in range(N):
    a=list(map(int,input().split()))
    A.append(a)
for i in range(N):
    result*=sum(A[i])
print(str(result%(10**9+7)))


