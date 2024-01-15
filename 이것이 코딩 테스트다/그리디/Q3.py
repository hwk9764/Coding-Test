'''seq = list(map(int, list(input())))

num_1 = sum(seq)
num_0 = len(seq) - num_1

answer = 0
state = False
# 0 뒤집기
if num_1 >= num_0:
    for i in range(num_0 + num_1):
        # 0이 처음 나오면 연속으로 0이 나오는지 세기 시작
        if seq[i] == 0:
            state = True
            seq[i] = 1
        # 0을 계속 세다가 1이 나오면
        elif seq[i] == 1 and state is True:
            state = False
            answer += 1
# 1 뒤집기
else:
    for i in range(num_0 + num_1):
        # 0이 처음 나오면 연속으로 0이 나오는지 세기 시작
        if seq[i] == 1:
            state = True
            seq[i] = 0
        # 0을 계속 세다가 1이 나오면
        elif seq[i] == 0 and state is True:
            state = False
            answer += 1

print(answer)
'''
# 좀 더 간략한 버전 (답안)
seq = input()
num_0 = 0
num_1 = 0

# 아래 반복문 때문에 맨 마지막 원소에 대해서는 바꾸는 경우를 셀 수 없으므로
# 맨 마지막 수를 확인해서 그냥 1 더해버림. 무조건 바뀐다고 가정하고
# 이렇게 해도 min으로 따지기 때문에 답은 올바르게 나옴
if seq[-1] == '0':
    num_0 = 1
else:
    num_1 = 1

for idx in range(len(seq)-1):
    # 숫자가 바뀔 때
    if seq[idx] != seq[idx+1]:
        # 1로 바뀌면 0을 뒤집을 때를 상정하여 카운트
        if seq[idx+1] == '1':
            num_0 += 1
        # 0으로 바뀌면 1을 뒤집을 때를 상정하여 카운트
        else:
            num_1 += 1
print(num_0, num_1)
print(min(num_0, num_1))