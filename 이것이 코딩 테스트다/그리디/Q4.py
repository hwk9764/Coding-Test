n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
total = sum(coins)
nums = [1] + [0] * total
nums[-1] = 1

# 가지고 있는 동전들로 만들 수 있는 가장 큰 값부터 하나하나 따져가기
for i in range(total, 0, -1):
    rest = i
    for coin in coins:
        if rest >= coin:
            rest -= coin
    if rest == 0:
        nums[i] = 1
print(nums.index(0))

# 답지 => 얘가 좀 더 천재적인 발상인 듯
# ★ 현재 동전으로 1부터 target까지 모든 수를 만들 수 있다고 할 때 ★
# 다음에 target보다 작거나 같은 수 아무거나(n) 추가하면 1부터 target+n까지의 수를 모두 만들 수 있음.
# 신기
target = 1
for coin in coins:
    # target은 만들고자 하는 수. target이 남은 동전보다 작을 경우 target은 남은 동전들로 만들 수 없음을 뜻함.
    if target < coin:
        # target이 정답
        break
    # target이 남은 동전보다 클 경우에는 남은 동전으로 만들 수 있음.
    target += coin
print(target)