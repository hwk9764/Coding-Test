inf = int(1e3)
n, m = map(int, input().split())
graph = [[inf]*(n+1) for _ in range(n+1)]

# 자기 자신과의 연결은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 노드 간의 직접적인 연결이 있으면 거리를, 없으면 inf를 저장
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

# x는 최종 목적지, k는 경유지
x, k = map(int, input().split())

# i, j는 시작지, j는 도착지, k는 경유지
# 경유지를 거쳐 가는 것이 직접적으로 가는 것보다 빠른 경우 그 경유지를 거치는 거리로 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        for node in range(i, j+1):
            graph[i][j] = min(graph[i][j], graph[i][node]+graph[node][j])

# 1부터 k까지의 최단거리 + k부터 x까지의 최단거리 => 1부터 x까지의 최단 거리와 같을 수 밖에
distance = graph[1][k] + graph[k][x]

# 어떤 식으로든 도달할 수 없다면 inf보다 큼.
if distance >= inf:
    print(-1)
else:
    print(distance)


