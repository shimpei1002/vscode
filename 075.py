from math import sqrt

def factorization(n):
    factors = []
    if n == 1:
        return [1]

    n1 = n
    for i in range(2, int(sqrt(n))+1):
        if n1 % i == 0:
            while n1 % i == 0:
                n1//=i
                factors.append(i)
                if n1 == 1:
                    return factors
    if n1 != 1:
        factors.append(n1)
        return factors
    elif factors == []:
        return [n]
N=int(input())
A=factorization(N)
sum=0
i=0
if(len(A)==1):
    print('0')
else:
    while(len(A)>2**i):
        i+=1
    print(i)

