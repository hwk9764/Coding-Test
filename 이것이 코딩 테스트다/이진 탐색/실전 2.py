# 이진 탐색 방법
n = int(input())
merchs = sorted(list(map(int, input().split())))
m = int(input())
ask = list(map(int, input().split()))

def search(start, end, to_find):
    mid = (start + end) // 2
    if start > end:
        return None
    if to_find == merchs[mid]:
        return merchs[mid]
    if to_find > merchs[mid]:
        return search(mid+1, end, to_find)
    if to_find < merchs[mid]:
        return search(start, mid-1, to_find)

for com in ask:
    print('no' if (None == search(0, n-1, com)) else 'yes', end=' ')

# 계수 정렬 방법
n = int(input())
inven = [0] * (n+1)
for ele in input().split():
    inven[int(ele)] += 1
m = int(input())
ask = list(map(int, input().split()))

for a in ask:
    if inven[a] != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 집합 자료형
n = int(input())
merchs = set(list(map(int, input().split())))
m = int(input())
ask = list(map(int, input().split()))

for i in ask:
    if i in merchs:
        print('yes', end=' ')
    else:
        print('no', end=' ')
