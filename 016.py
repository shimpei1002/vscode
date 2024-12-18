N = int(input())
A, B, C = map(int, input().split())
coca = [A, B, C]
coca.sort(reverse=True)
ans = float('inf')

for i in range(N // coca[0] + 1):
    for j in range((N - i * coca[0]) // coca[1] + 1):
        remaining = N - i * coca[0] - j * coca[1]
        if remaining % coca[2] == 0:
            k = remaining // coca[2]
            ans = min(ans, i + j + k)

print(ans)
