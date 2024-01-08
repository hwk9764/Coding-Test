import heapq

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

n, m = map(int, input().split())
parent = [0] * (n+1)

# root 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

unions = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(unions, (c, a, b))

cost = 0
history = 0
while unions:
    c, a, b = heapq.heappop(unions)
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_parent(a, b)
        cost += c
        history = c

cost -= history
print(cost)