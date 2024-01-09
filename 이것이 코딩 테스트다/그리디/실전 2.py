N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums = sorted(nums, reverse=True)
est, sec = nums[0], nums[1]

result = 0

# 1
m = 0
while True:
    rest = (M-m) % K
    if rest < K:
        result += est * rest
        break
    elif m == M:
        break
    result += est * K + sec
    m += K + 1

# 2
k = 0
for _ in range(M):
    if k == K:
        result += sec
        k = 0
        continue
    k += 1
    result += est

print('result = ', result)