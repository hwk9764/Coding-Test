n = int(input())
dp = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    dp[i] = line

for idx in range(1, len(dp)):
    for jdx in range(len(dp[idx])):
        # 그 줄의 맨 첫 숫자일 때
        if jdx == 0:
            dp[idx][jdx] += dp[idx-1][jdx]
        # 그 줄의 맨 뒤 숫자일 때
        elif jdx == idx:
            dp[idx][jdx] += dp[idx-1][jdx-1]
        # 그 외에는 왼쪽 위와 오른쪽 위의 값을 비교해 더 큰 값과 더함
        else:
            dp[idx][jdx] += max(dp[idx - 1][jdx-1], dp[idx - 1][jdx])
print(max(dp[-1]))