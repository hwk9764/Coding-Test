# 다익스트라 (가중치가 다양하기 때문에 bfs 못 씀)
import heapq

def daic(graph, n):
    # 최단 거리로 이동하는 정점들을 heap에 저장함. => 모든 정점을 거치지 않음
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    # 한 번 방문한 정점은 다시 방문하지 않음
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    # 각 정점까지의 최소 cost를 개별 리스트에 저장함. (0, 0)은 그래프에서 가져옴
    distance = [[inf] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    # 상하좌우로만 움직일 수 있음.
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]
    while heap:
        # cost, 현재 좌표를 heap에서 꺼내어 현재 좌표의 최단 거리가 heap에서 꺼낸 cost보다 적으면 연산하지 않음
        c, x, y = heapq.heappop(heap)
        if distance[x][y] < c:
            continue
        # 상하좌우 한 번씩 이동하며 최단 거리를 업데이트하고, 최단 거리에 있는 정점으로만 움직임
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                distance[nx][ny] = min(distance[nx][ny], distance[x][y] + graph[nx][ny])
                visited[nx][ny] = True
                # (n-1, n-1)에 도달했을 시 다른 경로는 계산하지도 않고 끝내버림
                if nx == n-1 and ny == n-1:
                    print(distance[n-1][n-1])
                    return
                heapq.heappush(heap, (distance[nx][ny], nx, ny))


inf = int(1e3)
T = int(input())

for _ in range(T):
    graph = []
    n = int(input())
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    daic(graph, n)

