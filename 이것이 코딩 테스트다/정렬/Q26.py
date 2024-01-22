# 이 알고리즘의 핵심 아이디어는 합친 카드묶음을 새로운 카드묶음으로 간주하고 다시 묶기를 수행하는 것
# 예를 들어 2, 2, 3, 4 이렇게 시작한다고 치면, 여기선 2, 2를 합치고
# 그 다음에는 3, 3, 4 이렇게 시작한다고 치고, 여기선 3, 3을 합치고
# 그 다음에는 4, 6 이렇게 시작한다고 치고, 4, 6을 합친다.
import heapq
n = int(input())
sequence = []
for _ in range(n):
    heapq.heappush(sequence, int(input()))

result = 0
while(len(sequence) != 1):
    one = heapq.heappop(sequence)
    two = heapq.heappop(sequence)
    sum_value = one + two
    result += sum_value
    heapq.heappush(sequence, sum_value)
print(result)