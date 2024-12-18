import itertools
N,P,Q=map(int,input().split())
A=list(map(int,input().split()))
sum=0
A=list(map(lambda x:x%P,A))
for pair in itertools.combinations(A,5):
    if(pair[0]*pair[1]%P*pair[2]%P*pair[3]%P*pair[4]%P==Q):
        sum+=1
print(str(sum))