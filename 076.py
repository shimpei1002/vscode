N = int(input())
A = list(map(int, input().split()))
total = sum(A)

# totalが10で割り切れない場合は「No」を出力
if total % 10 != 0:
    print('No')
else:
    d = total // 10
    A = A + A  # リストAを複製して扱う

    # スライディングウィンドウを使った探索
    current_sum = 0
    start = 0
    found = False

    for end in range(2 * N):
        current_sum += A[end]

        while current_sum > d and start <= end:
            current_sum -= A[start]
            start += 1

        if current_sum == d and end - start + 1 <= N:
            found = True
            break

    print('Yes' if found else 'No')

