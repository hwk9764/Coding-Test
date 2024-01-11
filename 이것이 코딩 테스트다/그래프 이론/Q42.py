# 처음에 푼 데이터 크기 커지면 시간 오래 걸리는 풀이
'''
def docking():
    for _ in range(p):
        gate = int(input())
        # 순차적으로 확인하며 빈 곳을 찾음
        for i in range(gate, 0, -1):
            if gates[i] == 0:
                gates[i] = 1
                break
            if i == 1:
                return
g = int(input())
p = int(input())
gates = [0] * (g+1)
docking()
print(sum(gates))
'''
# union-find 방법 사용
# 도킹은 제일 큰 숫자의 차고에 하는 것을 원칙으로 함. 차있다면, 그 차고의 parent가 0이 아닐시 거기에 도킹하도록 함.
# 가능한 차고가 남아있을 시(gate의 parent가 0이 아닐 시), 그 차고와 그 밑의 차고를 union함.
# gate의 parent가 0이면 gate 이하 차고가 모두 다 찼다는 것을 의미함.
def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

g = int(input())
p = int(input())
parents = [0] * (g+1)

# 자기 자신으로 부모 초기화
for i in range(g+1):
    parents[i] = i
answer = 0
for _ in range(p):
    gate = int(input())
    # gate의 parent가 0이 아니면 도킹할 차고가 남았다는 것
    # 그럼 parent와 그 밑에를 연결해야 함.
    parent = find_parent(gate)
    if parent != 0:
        union_parent(parent, parent-1)
        answer += 1
    else:
        break
print('최종 : ', parents)
print(answer)