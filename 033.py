H,W=map(int,input().split())
yoko=(H//2)+(H%2)
tate=(W//2)+(W%2)
if(H==1 or W==1):
    print(str(H*W))
else:
    print(str(yoko*tate))