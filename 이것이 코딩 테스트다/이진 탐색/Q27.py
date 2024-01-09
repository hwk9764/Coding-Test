from copy import deepcopy
import random
import time

n, x = map(int, input().split())
#graph = list(map(int, input().split()))
graph = [random.randint(1, 100) for _ in range(n)]
graph.sort()
'''
mid가 x값들의 중간에 오면 골치아파져서 mid가 x값이면 지우고 다시 탐색하는 방법을 써봤는데 그러니까 10^6개의 데이터에선 데이터의 수만큼 탐색이 반복되어서 시간이 좀 걸리더라

start = 0
end = len(graph) - 1
temp = deepcopy(graph)
answer = 0
while start < end:
    mid = (start + end) // 2
    if temp[mid] == x and len(temp) > 1:
        temp.pop(mid)
        end -= 1
        answer += 1
    elif temp[mid] < x:
        start = mid + 1
    else:
        end = mid

print(answer)
'''

# 그래서 처음과 끝의 index를 구해서 둘의 차로 계산하는 게 올바른 솔루션이라는 것 같음
# ★이 문제와 관계 없이 이진탐색트리 문제는 꼭 정답 index를 찾으면 거기서 탐색은 멈추도록 짜기★

def find_start():
    temp = deepcopy(graph)
    start = 0
    end = len(temp) - 1
    while start < end:
        mid = (start + end) // 2
        if temp[mid] == x and (mid == 0 or temp[mid-1] < x):
            return mid
        if temp[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return start if temp[start] == x else None

def find_end():
    temp = deepcopy(graph)
    start = 0
    end = len(temp) - 1
    while start < end:
        mid = (start + end) // 2
        if temp[mid] == x and (mid == n-1 or temp[mid+1] > x):
            return mid

        if temp[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return end if temp[end] == x else None

begin = time.time()
start = find_start()

if start == None:
    result = -1
else:
    end = find_end()
    result = end - start + 1

e = time.time()
print(result)
print(e-begin)
