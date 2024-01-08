n, m = map(int, input().split())
dducks = sorted(list(map(int, input().split())))
length = range(dducks[0], dducks[-1]+1)

def search(start, end):
    if start > end:
        return length[start]

    mid = (start + end) // 2
    total = 0
    for dduck in dducks:
        if dduck >= length[mid]:
            total += (dduck - length[mid])

    if total < m:
        return search(start, mid-1)
    if total >= m:
        return search(mid + 1, end)

print(search(0, n))