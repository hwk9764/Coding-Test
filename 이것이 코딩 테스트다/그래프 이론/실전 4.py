# 개망함 아 나중에 할래
# 밑에는 그냥 답지 퍼옴..
from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
indegree = [0] * (n+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range (1, n + 1):
	data = list(map(int, input().split()))
	times[i] = data [0] # 첫 번째 수는 시간 정보를 담고 있음
	for x in data [1:-1]:
		indegree[i] += 1
		graph[x].append(i)
# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(times) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0 인 노드를 큐에 삽입
    for i in range (1, n+1):
        if indegree[i]==0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft() # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0 이 되는 노드를 큐에 삽입
            if indegree[i] == 0 :
                q.append (i)
    # 위상 정렬을 수행한 결과 출력
    for i in range (1, n + 1):
        print(result[i])
topology_sort()