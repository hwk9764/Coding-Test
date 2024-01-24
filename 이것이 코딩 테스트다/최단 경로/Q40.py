# 문제에서 bfs로 하면 쉬운데 다익스트라로 풀어보래서 풀어봄. 밑에 일부 빼곤 다 제대로 구현함
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

heap = []
heapq.heappush(heap, (0, 1))    # 거리, 정점
inf = int(1e9)
distances = [inf]*(n+1)
distances[1] = 0

while heap:
    distance, node = heapq.heappop(heap)
    if distances[node] < distance:
        continue
    for i in graph[node]:
        #distances[i] = min(distances[i], distances[node]+1)
        #heapq.heappush(heap, (distances[i], i))

        # 거리가 1인데 억지로 다익스트라 쓰려니 코드가 복잡해짐
        # for문 안을 이렇게 바꿔야 함.
        if distances[node]+1 < distances[i]:
            distances[i] = distances[node]+1
            heapq.heappush(heap, (distances[i], i))
print(distances)

# bfs로 하면 이렇게 간단한걸...
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
distances = [0] * (n+1)
visited = [False] * (n+1)
visited[1] = True
q = deque([1])
count = 0
while q:
    node = q.popleft()
    for i in graph[node]:
        if visited[i] == False:
            visited[i] = True
            distances[i] = distances[node] + 1
            q.append(i)

first = distances.index(max(distances))
second = distances[first]
third = distances.count(second)
print(first, second, third)