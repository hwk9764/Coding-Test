'''
i번째 날의 최대 수입은 i번째 날의 상담을 진행할 시 수입 + i번째 날의 상담이 끝난 후 그 다음 날부터 마지막날까지의 최대 수입
따라서 뒤에서부터 dp하는 방법을 사용하여 구할 수 있음.
'''
n = int(input())
graph = []
dp = [0] * (n+1)
for i in range(1, n+1):
    graph.append(tuple(map(int, input().split())))

for i in range(n, 0, -1):
    if graph[i-1][0] + i <= n+1:
        next = i + graph[i-1][0]
        # i번째 날의 최대 수입은 (i번째 날 상담의 수입 + i번째 날 상담 기간 후의 최대 수입)과 i번째 상담을 하지 않을 때의 최대 수입 중 최댓값
        dp[i] = max(graph[i-1][1]+dp[next], dp[i-1])
    else:
        dp[i] = dp[i-1]

print(dp)