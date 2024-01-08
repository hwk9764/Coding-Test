inf = 1e3
city = int(input())
bus = int(input())
# graph는 버스 시작 도시, 도착 도시, 버스비 3가지로 이루어져 있음
graph = [list(map(int, input().split())) for _ in range(bus)]
routes = [[inf]*(city+1) for _ in range(city+1)]

# 각 원소가 도시간 최단 거리를 나타내는 n by n 리스트를 출력

# 자기 자신까지 최단거리 0으로 초기화
for i in range(1, city+1):
    routes[i][i] = 0
# 도시 사이 거리 초기화
for depart, destination, dis in graph:
    routes[depart][destination] = min(routes[depart][destination], dis)

# ★for문의 첫번째는 무조건 경유지로 하기★
# 경유지가 맨 마지막으로 가면 이동은 아직 앞쪽에서 하려고 하는데 경유지가 아직 업데이트 되지 않은 뒤쪽의 정보를 필요로 하는 경우가 생김
# 하지만 첫번째로 온다면 시작과 끝이 가변하더라도 경유지가 차근차근 올라가기 때문에 값을 빼먹지 않고 제대로 업데이트하게 된다.
# 어차피 우리의 주 목적은 시작->끝의 최단 거리를 재고자 하는 것이기 때문에 미래의 값을 사용할 가능성은 경유지밖에 없음.
# ★★ 시작->끝은 우리가 업데이트해야 할 대상이고 경유지는 확정되어 있는 값이어야 하기 때문에 ★★
for k in range(1, city+1):
    for i in range(1, city+1):
        for j in range(1, city+1):
            if i==j or i==k or j==k:
                continue
            routes[i][j] = min(routes[i][j], routes[i][k]+routes[k][j])

for route in routes:
    print(route)