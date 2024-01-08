# n : 학생 수, m : union 수
n, m = map(int, input().split())
roots = [0] * (n+1)

# root 자기 자신으로 초기화
for i in range(1, n+1):
    roots[i] = i
def combine_union(a, b):
    a = find_union(a)
    b = find_union(b)
    if a < b:
        roots[b] = a
    else:
        roots[a] = b

def find_union(x):
    '''if roots[a] == roots[b]:
        return True
    else:
        return False'''
    if roots[x] != x:
        roots[x] = find_union(roots[x])
    return roots[x]

for _ in range(m):
    state, a, b = map(int, input().split())
    # combine
    if state == 0:
        combine_union(a, b)
    else:
        if find_union(a) == find_union(b):
            print('YES')
        else:
            print('NO')
        #print('YES' if result else 'NO')