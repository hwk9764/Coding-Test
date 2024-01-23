# 최장 길이 부분 수열 찾기 유형
# D[i]는 array[i]를 마지막 원소로 가지는 부분 수열의 가능한 최대 길이라고 할 때
# D[i]의 점화식은 D[i] = max(D[i], D[j]+1) (단, j<i, D[j]의 부분 수열에 i를 추가하므로 +1) 이라고 한다.
n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()
dp = [1] * n
for i in range(n):
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))