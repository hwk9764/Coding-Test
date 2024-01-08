n = int(input())
people = list(map(int, input().split()))
people.sort(reverse=True)
answer = 0
idx = 0
# 그룹 만들지 못한 나머지 사람들
restofp = len(people)
while(people[idx] <= restofp):
    num = people[idx]
    answer += 1
    idx += num
    if idx > len(people)-1:
        break
    restofp -= idx

print(answer)