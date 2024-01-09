num = int(input())
warehouse = [0] + list(map(int, input().split()))

dp = [0] * (num+1)
for i in range(1, num+1):
    if i == 1 or i == 2:
        dp[i] == warehouse[i]
    if i == 3:
        dp[i] = warehouse[1] + warehouse[i]
    dp[i] = warehouse[i] + max(dp[i-2], dp[i-3])

print(max(dp))

# 정답
dp[0] = warehouse[0]
dp[1] = max(warehouse[0], warehouse[1])

for i in range(3, num+1):
    dp[i] = max(dp[i-1], dp[i-2] + warehouse[i])