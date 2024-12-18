from itertools import permutations
N=int(input())
A=[[] for _ in range(N)]
g=[]
for i in range(N):
    A[i]=list(map(int,input().split()))
    g.append(i)
M=int(input())
X=[]
Y=[]
kenaku=[[0]*N for _ in range(N)]
for i in range(M):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
    kenaku[i-1][j-1]=1
    kenaku[j-1][i-1]=1
Answer=1000000000000
for pair in list(permutations(g)):
    sum=0
    check=0
    for i in range(N-1):
        sum+=A[pair[i]][i]
        if(kenaku[pair[i]][pair[i+1]]==1):
            check=1
            break
    if(check==0):
        sum+=A[pair[N-1]][N-1]
        if(Answer>sum):
            Answer=sum
if(Answer==1000000000000):
    print('-1')
else:
    print(str(Answer))