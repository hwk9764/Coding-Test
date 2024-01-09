N, M = map(int, input().split())
lists = []
for _ in range(N):
    elem = list(map(int, input().split()))
    elem = min(elem)
    lists.append(elem)
print((max(lists)))