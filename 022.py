import math
A,B,C=map(int,input().split())
gcd=math.gcd(A,B,C)
print(str((A//gcd-1)+(B//gcd-1)+(C//gcd-1)))