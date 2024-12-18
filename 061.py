Q=int(input())
T,X=[],[]
for _ in range(Q):
    t,x=map(int,input().split())
    T.append(t)
    X.append(x)
tehuda=[]
for i in range(Q):
    if(T[i]==1):
        tehuda.insert(0,X[i])
    elif(T[i]==2):
        tehuda.append(X[i])
    else:
        print(str(tehuda[X[i]-1]))
