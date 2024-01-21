#from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
answer = -1

# for문으로 len(a)만큼 반복시키면 큰일 남
# 업앤다운 게임방식으로 하기
def binary_search(start, end):
    while True:
        if start > end:
            return -1

        mid = (start+end)//2
        if a[mid] == mid:
            return mid
        # 좌측 버리기
        elif a[mid] < mid:
            start = mid + 1
            continue
        # 우측 버리기
        elif a[mid] > mid:
            end = mid - 1

answer = binary_search(0, n-1)
print(answer)


