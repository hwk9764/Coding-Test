import time
from collections import deque
N, M = map(int, input().split())
graph = [[1]*(M+1)]

for _ in range(N):
    data = [1] + list(map(int, input()))
    graph.append(data)
queue = deque([(1, 1)])
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if 0 < nx <= N and 0 < ny <= M and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print('result : ', graph[N][M])

'''
처음에 실전 3처럼 result=0으로 두고 탐색 한번 할 때마다 +1씩 했는데
그렇게 하니까 길이 조금만 복잡해지면 답이 달라짐
그래서 이전 노드 값 + 1로 해서 목표지점의 값을 출력하는 걸로 하기
'''