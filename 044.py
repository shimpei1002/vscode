N,Q=map(int,input().split())
A=list(map(int,input().split()))
T,X,Y=[],[],[]
shift=0
for _ in range(Q):
    t,x,y=map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
for i in range(Q):
    if(T[i]==1):
        x=(X[i]-1-shift)%N
        y=(Y[i]-1-shift)%N
        A[x],A[y]=A[y],A[x]
    elif(T[i]==2):
        shift+=1
    else:
        g=(X[i]-1-shift)%N
        print(str(A[g]))