import heapq
# n은 도시의 개수, m은 통로의 개수, k는 메세지를 보내는 도시 즉, 시작점.
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = int(1e3)
distance = [inf]*(n+1)

for _ in range(m):
    # x, y는 도시, z는 x->y 통로의 메세지 전송 시간
    x, y, z = map(int, input().split())
    # 안헷갈리게 heap 입력 순서랑 같게 함
    graph[x].append((z, y))

distance[k] = 0
heap = []
# heap에 (k부터 도착 노드까지의) 거리, 도착 노드 순으로 넣음.
heapq.heappush(heap, (0, k))
while heap:
    # dis : k부터 now까지의 거리, now : 현재 노드
    dis, now = heapq.heappop(heap)

    # 지난번에 구한 now까지의 거리가 힙에 저장되어 있던 거리보다 작으면 이미 최단거리를 찾은 것이므로 연산 안함
    # 밑에 for문을 한번이라도 덜 돌기 위함
    if distance[now] < dis:
        continue

    # k부터 des까지의 거리 d
    for d, des in graph[now]:
        # cost : k부터 현재 노드까지 최단거리 + 현재 노드부터 목적지인 des까지 거리
        # => k->now + now->des
        cost = distance[now] + d
        # k부터 des까지의 거리와 위에서 구한 cost 중 작은 값을 저장
        distance[des] = min(distance[des], cost)
        heapq.heappush(heap, (distance[des], des))

print(distance)
print('메세지를 받는 도시의 수 : ', len([i for i in distance if i != inf])-1)
print('메세지가 도달하는데 걸리는 시간 : ', max([i for i in distance if i != inf]))

'''
예시 입력
3 2 1
1 2 4
1 3 2
=> [1000, 0, 4, 2]
메세지를 받는 도시의 수 :  2
메세지가 도달하는데 걸리는 시간 :  4

7 10 3
1 2 4
3 1 2
4 1 2
7 1 7
5 2 1
6 2 3
4 3 2
3 6 2
4 7 3
6 5 2
=> [1000, 2, 5, 0, 1000, 4, 2, 1000]
메세지를 받는 도시의 수 :  4
메세지가 도달하는데 걸리는 시간 :  5
'''