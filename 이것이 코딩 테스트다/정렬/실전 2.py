num = int(input())
nums = []
for _ in range(num):
    number = int(input())
    nums.append(number)

# 퀵 정렬
def quick(start, end):
    if start >= end:
        return
    pivot = start
    left = end
    right = start + 1
    while left >= right:
        # 작은 놈 찾기
        while nums[pivot] <= nums[left] and left > start:
            left -= 1
        # 큰 놈 찾기
        while nums[pivot] >= nums[right] and right < end:
            right += 1

        # 엇갈렸을 때 => 작은 놈들과 큰 놈들이 제대로 모였을 때만 엇갈림.
        if left < right:
            nums[pivot], nums[left] = nums[left], nums[pivot]
        else:
            nums[left], nums[right] = nums[right], nums[left]

    quick(start, left-1)
    quick(left+1, end)

quick(0, num-1)
print(nums)