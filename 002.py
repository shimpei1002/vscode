from itertools import product
def isvaild(S):
    score=0
    for c in S:
        if c=='(':
            score+=1
        else:
            score-=1
        if score<0:
            return False
    return (score==0)
N=int(input())
for S in product(['(',')'],repeat=N):
    if(isvaild(S)):
        print(*S,sep='')