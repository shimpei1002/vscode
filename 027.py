N=int(input())
S=[]
for _ in range(N):
    s=str(input())
    S.append(s)
H=set()
print('1')
H.add(S[0])
for i in range(1,N):
    if S[i] not in H:
        print(str(i+1))
        H.add(S[i])