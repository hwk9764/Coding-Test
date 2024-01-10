'''
풀이 아이디어
비교에 따라 연결해서 그래프를 만든 다음, 한 정점에서 다른 모든 정점에 각각 도달하거나 반대로 도달될 수 있다면
순위 비교가 가능하다고 함.
예를 들어, 이 문제의 테스트 케이스인
6 6
1 5
3 4
4 2
4 6
5 2
5 4에서 그래프를 그려보면 4에서 2, 6으로 연결되어있고, 1, 3, 5에서 4로 연결되어 있음
나머지는 연결이 안되는 정점이 존재함. 예를 들면 3같은 경우 4랑밖에 연결이 되어 있지 않음
따라서 4의 순위를 정확하게 알 수 있음.
=> 플로이드 워셜 알고리즘을 이용해 각 정점이 다른 모든 정점들과 연결되어 있는지 확인할 수 있음.

※ 여기서 의문, 굳이 플로이드 워셜을 사용해서 최소 거리를 구해서 이렇게 할 필요가 있나?
그냥 대충 연결되어 있는지만 구하면 되는거 아닌가 => 됨. 아주 잘 됨.
'''
n, m = map(int, input().split())
grades = [[] for _ in range(n+1)]

inf = 1e5
arr = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    grades[a].append(b)
    arr[a][b] = 1

# 자기 자신의 거리는 0으로 초기화
for idx in range(n+1):
    arr[idx][idx] = 0

# 플로이드 워셜 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        if i==k:
            continue
        for j in range(1, n+1):
            if j==k:
                continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            # 굳이 최소거리를 구해야 하나? 그냥
            #if arr[i][k] != inf and arr[k][j] != inf:
            #    arr[i][j] = 1 or True
            # 이렇게 하면 안되는 건가?
            # 됨. 아주 잘 됨.


# 각 정점이 다른 정점과 모두 연결되어 있는지 확인
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if arr[i][j] != inf or arr[j][i] != inf:
            count += 1
    if count == n:
        result += 1

print(result)