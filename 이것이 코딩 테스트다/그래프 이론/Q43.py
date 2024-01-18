# 어떻게든 연결만 되게 -> union-find 거의 공식
# 크루스칼 알고리즘인데 얘는 그리디를 기반으로하는 최소 비용 구하기 문제
# heap에 모두 넣고 제일 적은 비용부터 빼서 연결한다.
# parent를 비교해서 이미 연결되어 있다면 고려하지 않고 넘긴다.
import heapq
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a <= b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int, input().split())
heap = []
summation = 0
cost = 0
parents = [0] * n
for i in range(n):
    parents[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    summation += z
    heapq.heappush(heap, (z, x, y))
    # (x:집, y:집, z:집간 길이)

while heap:
    z, x, y = heapq.heappop(heap)
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x != y:
        union_parent(parents, x, y)
        cost += z
print(summation - cost)