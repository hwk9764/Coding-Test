n = int(input())
stages = list(map(int, input().split()))


def solution(N, stages):
    num_people = len(stages)
    count = [0] * (N+1)  # 각 stage마다 사람이 몇 명 머물러 있는지
    num = [num_people] * (N+1)   # 각 stage를 통과한 사람이 몇 명인지
    for stage in stages:
        # count 최신화
        if stage <= N:
            count[stage] += 1
    # 실패율, stage로 구성되어 내림차순 할 리스트
    answer = [0] * N
    for i in range(1, N+1):
        # num 최신화. 이전 num - count가 현재 num이다.
        num[i] = num[i-1] - count[i-1]
        answer[i-1] = (-count[i] / num[i], i)
    answer.sort()
    return answer

answer = solution(n, stages)
print('answer : ', answer)
for a in answer:
    print(a[-1], end=' ')

'''
count 함수를 활용한 풀이

def solution(N, stages):
    answer = []
    num_people = len(stages)

    for i in range(1, N+1):
        # 사람이 하나도 없으면 실패율도 0인 것
        if num_people == 0:
            answer = [i for i in range(1, N+1)]
            return answer
        # stages 안에 i 단계에 머무른 사람이 몇 명 있는지
        count = stages.count(i)
        answer.append((count/num_people, i))    # 실패율, stage num 리스트에 추가
        num_people -= count # 내 코드 num-count와 같은 연산
    return sorted(answer, key=lambda x:-x[0])

answer = solution(n, stages)
for a in answer:
    print(a[-1], end=' ')
'''