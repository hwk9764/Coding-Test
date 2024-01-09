# n : 총 도시 수, m : 방문할 도시 수(중복 허용)
n, m = map(int, input().split())
parents = [0] * (n+1)

# root를 자기 자신으로 초기화
for i in range(1, n+1):
    parents[i] = i

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a, b):
    # 처음에 쓴 코드는 if parents[a] < parents[b]: , if a<b: ~~
    # 그냥 바꾸면 타고 올라가 root를 찾는 것이 아니라 그냥 서로의 이름만 교환하게 됨
    # 그래서 find_parent로 root를 찾아주기
    a = find_parent(parents[a])
    b = find_parent(parents[b])
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(n):
    for j, state in enumerate(map(int, input().split())):
        if state == 1:
            # find 쓸 필요 없이 그냥 parent로만 해도 됨. union에서 어차피 find하니까
            # 원래 내가 쓴 코드 : if find_parents(i+1) != find_parents(j+1):
            if parents[i+1] != parents[j+1]:
                union_parent(i+1, j+1)

plan = list(map(int, input().split()))

result = 'Yes'
for idx in range(len(plan)-1):
    if parents[plan[idx]] != parents[plan[idx+1]]:
        result = 'No'

print(parents)
print(result)