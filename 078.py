N, M = map(int, input().split())
degree = [0] * N  # 各頂点の次数を保持するリスト

for _ in range(M):
    a, b = map(int, input().split())
    if(a>b):     
        degree[a - 1] += 1
    else:
        degree[b - 1] += 1

ans = sum(1 for d in degree if d == 1)
print(ans)