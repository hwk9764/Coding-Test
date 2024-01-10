# 정답 코드로 돌려도 8 by 8 데이터가 엄청 오래 걸린다.
# 파이참이라서 이러는건가? 시간 제한이 2초인데 어떻게 정답 코드로도 한참이 걸리는지
# 내 코드도 최대한 비슷하게 구현했는데 시간이 너무 오래 걸리길래 틀린 줄 알았는데
# 정답 코드 돌려보니 그렇진 않은 것도 같다. 모르겠다.
# ★백준 연구소 파일에 코드처럼 풀기. 그 방법이 훨씬 시간이 덜 든다.★
import time
# 바이러스 전파 후 0 개수 출력

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]
def virus(copy_graph, q):
    #temp_q = deepcopy(q)    # deecopy가 엄청 오래 걸림. 그냥 쓰지마 시벌
    temp_q = []
    for dc in q:
        temp_q.append(dc)
    while temp_q:
        now = temp_q.pop()
        for dr, dc in zip(drs, dcs):
            nr = now[0] + dr
            nc = now[1] + dc
            if 0<=nr<n and 0<=nc<m:
                if copy_graph[nr][nc] == 0:
                    copy_graph[nr][nc] = 2
                    temp_q.append((nr, nc))

    return find_clean(copy_graph)

# 벽을 세우고 virus 실행
def dfs(q, count):
    global result
    if count == 3:
        #copy_graph = deepcopy(graph)    # deecopy가 엄청 오래 걸림. 데이터 크기가 크면 쓰지 않기
        for i in range(n):
            for j in range(m):
                copy_graph[i][j] = graph[i][j]

        result = max(result, virus(copy_graph, q))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(q, count)
                graph[i][j] = 0
                count -= 1

# 0 개수 찾기
def find_clean(copy_graph):
    score = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                score += 1
    return score

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    copy_graph = [[0] * m for _ in range(n)]
    q = list()
    s = time.time()
    # 2 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))
    result = 0
    dfs(q, 0)
    print(result)
    print(time.time()-s)