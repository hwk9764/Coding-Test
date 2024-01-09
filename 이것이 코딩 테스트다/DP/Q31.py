from copy import deepcopy
def solution(map):
    dp = deepcopy(map)
    for j in range(2, m+1):
        for i in range(1, n+1):
            dp[i][j] += max(dp[i+1][j-1], dp[i][j-1], dp[i-1][j-1])

    result = 0
    for k in range(1, n+1):
        result = max(dp[k][m], result)
    return result

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    all_golds = list(map(int, input().split()))
    gold_map = [[0]*(m+1) for _ in range(n+2)]

    for i in range(1, n+1):
        gold_map[i] = [0] + all_golds[m*(i-1):i*m]
    print(solution(gold_map))