import time


# bfs 풀이
from collections import deque

start = time.time()

N, M = map(int, input().split())

cast = []
for _ in range(N):
    cast.append(map(int, input()))

visited = [[False]*M for _ in range(N)]
result = 0

def queue(q, visited):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs, dys):
            temp_r = r + dx
            temp_c = c + dy
            if -1 < temp_r < N and -1 < temp_c < M and cast[temp_r][temp_c] == 0 and visited[temp_r][temp_c] is False:
                visited[temp_r][temp_c] = True
                q.append((temp_r, temp_c))
    return visited

for r_idx, row in enumerate(cast):
    for e_idx, element in enumerate(row):
        if element == 0 and visited[r_idx][e_idx] is False:
            q = deque([(r_idx, e_idx)])
            visited[r_idx][e_idx] = True
            visited = queue(q, visited)
            result += 1

print('result : ', result)
end = time.time() - start
print(end)


# dfs
N, M = map(int, input().split())

cast = []
for _ in range(N):
    cast.append(input())

def dfs(r, c):
    stack.append((r, c))
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    # stack 버전
    while stack:
        r, c = stack.pop()
        for dx, dy in zip(dxs, dys):
            temp_r = r + dx
            temp_c = c + dy
            if -1 < temp_r < N and -1 < temp_c < M and cast[temp_r][temp_c] == 0 and visited[temp_r][temp_c] is False:
                stack.append((temp_r, temp_c))
                visited[temp_r][temp_c] = True
    # 재귀 버전
    for dx, dy in zip(dxs, dys):
        temp_r = r + dx
        temp_c = c + dy
        if -1 < temp_r < N and -1 < temp_c < M and cast[temp_r][temp_c] == 0 and visited[temp_r][temp_c] is False:
            visited[temp_r][temp_c] = True
            dfs(temp_r, temp_c)
    return

result = 0
stack = []
visited = [[False]*M for _ in range(N)]
for r_idx, row in enumerate(cast):
    for e_idx, element in enumerate(row):
        if element == 0 and visited[r_idx][e_idx] is False:
            dfs(r_idx, e_idx)
            result += 1

print('result : ', result)