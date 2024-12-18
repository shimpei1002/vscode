N,K=map(int,input().split())
if(K==1 and N>1):
    print('0')
elif(K==1 and N==1):
    print('1')
elif(K==2 and K>2):
    print('0')
elif(K==2):
    print('2')
else:
    result=K*(K-1)
    result*=(K-2)**(N-2)
    print(str(result%(10**9+7)))
