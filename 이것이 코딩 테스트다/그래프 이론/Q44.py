import heapq
n = int(input())
planets = []

parents = [0] * (n+1)
for i in range(1, n+1):
    parents[i] = i

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

# 처음 만든 코드
for _ in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

# 건설 비용이 적은 터널 순서대로 heap 정렬
# 모든 경우의 간선을 고려하기 때문에 연산량이 n(n-1)//2로 굉장히 커짐. => 효율적이지 못한 코드
heap = []
for i in range(n):
    for j in range(n):
        cost = min(abs(planets[i][0]-planets[j][0]), abs(planets[i][1]-planets[j][1]), abs(planets[i][2]-planets[j][2]))
        heapq.heappush(heap, (cost, i, j))   # 터널 건설 비용, 행성 좌표

answer = 0

while heap:
    cost, i, j = heapq.heappop(heap)
    if find_parent(i) != find_parent(j):    # 서로 연결되어 있지 않으면 연결하기
        union_parent(i, j)
        answer += cost

print(answer)

# 시간, 공간 복잡도를 개선한 코드
'''
모든 경우의 간선을 고려하면 메모리 초과가 발생함. n(n-1)//2개의 경우를 고려하게 되는데 n이 10^5라 최대 10^10까지 시간, 공간복잡도가 올라감
따라서 모든 경우를 고려하지 않고, 행성의 x, y, z 좌표들끼리 모아서 정렬한 다음, 인접한 좌표끼리 차(거리)를 구해 가장 작은 거리들을 구함.
즉, 1, 2끼리, 2, 3끼리, ... n-1, n끼리 거리를 구해서 총 n-1개의 cost를 계산한다. 그럼 3개의 좌표축이니까 3(n-1)개의 cost를 구하게 된다.
구한 cost들 3(n-1)개를 정렬해서 그 중 가장 작은 것들 n-1개를 뽑아 간선을 연결하고 최소 cost를 계산한다.
=> 이게 가능한 이유는 cost가 min(xa-xb, ya-yb, za-zb)이기 때문이다. cost는 각 좌표축에서의 거리 중 가장 작은 값이 되는데,
각 좌표값끼리 모아 최소 거리를 구한 값들은 cost 식 안에 들어가더라도 분명히 제일 작은 값이 될 것.
왜냐하면 모든 좌표값들의 차를 다 모아놓은 3(n-1)개를 정렬한 것 중에서도 가장 작은 값이기 때문에
'''
x = []
y = []
z = []
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort(), y.sort(), z.sort()

edges = []
for i in range(n-1):
    # 정렬한 후 인접한 좌표끼리의 차를 계산하기 때문에 최소값들만 모이게 됨.
    # 이번에는 x, y, z 따로가 아니라 모두 합치기 때문에 정렬시 두 행성간 통로의 cost라고 볼 수 있음.
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
edges.sort()

answer = 0
# 여기서 나오는 edge들은 min 안에 들어가서 연산되더라도 가장 작은 값이 될 수 밖에 없다.
for edge in edges:
    cost, i, j = edge
    if find_parent(i) != find_parent(j):
        union_parent(i, j)
        answer += cost
print(answer)