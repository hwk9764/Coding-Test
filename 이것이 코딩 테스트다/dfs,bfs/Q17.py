# n : 격자 크기, k : 바이러스 수
from collections import deque
n, k = map(int, input().split())
graph = [[-1] * (n+1)]
# virus_position이 dictionary면 안되는 이유 : 매 초마다 bfs를 맨 처음 바이러스의 위치에서만 수행하게 된다.
# 따라서 list로 만들고 sort해서 맨 마지막 위치에서 새로 bfs를 수행해야 함.
virus_position = []
q = deque()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append([-1] + row)
    # 현재 받은 행 data에 바이러스가 존재하면 위치 리스트에 추가
    for j in range(1, k+1):
        if j in row:
            virus_position.append((j, i+1, row.index(j)+1))
# s = s초, x, y : 결과 위치
s, x, y = map(int, input().split())

def bfs(q, virus):
    print(len(q))
    # 처음 들어온 q의 길이를 구해 새로 append된 data는 사용하지 않게끔 조치함.
    for _ in range(len(q)):
        # pop하기 전 맨 앞 data가 지금 다루려는 virus의 정보가 아닌 경우 바로 break
        if q[0][0] == virus:
            _, x, y = q.popleft()
            dxs = [-1, 1, 0, 0]
            dys = [0, 0, -1, 1]
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if 0<nx<=n and 0<ny<=n and graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, nx, ny))
        else:
            break
    return q

virus_position.sort()
# virus 정보 오름차순으로 정렬 후 q에 append
for v in virus_position:
    q.append(v)

# s초동안 모든 virus를 한번씩 전파시키기
for _ in range(s):
    for virus in range(1, k+1):
        q = bfs(q, virus)
print('graph : ', graph)
print(graph[x][y])