from collections import deque
# n : 도시의 개수
# m : 도로의 개수
# k : 거리
# x : 출발 도시
n, m, k, x = map(int, input().split())
graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)
q = deque([x])
distance = 0
answer = []
while q:
    now = q.popleft()
    distance += 1
    for des in graph[now]:
        if visited[des] is False:
            visited[des] = True
            q.append(des)
            if distance == k:
                answer.append(des)

print(answer if len(answer) != 0 else -1)