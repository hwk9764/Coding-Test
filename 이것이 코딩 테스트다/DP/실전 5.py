# n : 화폐 개수, m : 만들 금액
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [10001] * (m+1)    # m은 10000보다 작으므로 10001로 쓰레기값을 지정

for i in range(1, m+1):
    for coin in coins:
        if i == coin:
            dp[i] = 1
        else:
            dp[i] = min(dp[i-coin]+1, dp[i])

print(dp[m] if dp[m] != 10001 else -1)