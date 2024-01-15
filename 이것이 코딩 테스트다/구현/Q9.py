def solution(s):
    length = len(s)
    answer = length
    # 1부터 s의 길이 개수까지 반복 잘라보기
    for r in range(1, len(s)//2+1):
        prev = ''
        num = 1
        new = ''
        for i in range(length//r + 1):
            start = r * i
            end = r * (i+1)
            # 딱 r만큼의 길이만큼 자를 수 있을 때
            if end <= length:
                # 바로 전과 같은 조합이면 num에 +1
                if prev == s[start:end]:
                    num += 1

                # 처음 보는 조합이라면 prev 최신화, 이전 조합 new에 반영
                else:
                    # 맨 처음엔 그냥 넘겨야 함.
                    if prev != '':
                        new += str(num) + prev if num > 1 else prev
                    num = 1
                    prev = s[start:end]

                # 딱 r만큼 자를 수 있을 때 and 마지막 segment면
                if end == length:
                    if num != 1:
                        new += str(num) + prev
                    else:
                        new += s[start:]
                    break

            # 남은 길이가 r보다 작아서 r만큼 자를 수 없을 때
            elif start < length:
                new += prev + s[start:]

        answer = min(answer, len(new))
    return answer

if __name__ == '__main__':
    s = input()
    answer = solution(s)
    print(answer)

'''
답안 : 두 번째 for문을 좀 더 발전시켜 많은 if문이 필요하지 않도록

def solution(s):
    length = len(s)
    answer = length
    # 1부터 s의 길이 개수까지 반복 잘라보기
    for r in range(1, len(s)//2+1):
        # 이 부분 수정 prev = '' ->
        prev = s[0:r]
        num = 1
        new = ''
        # 이 부분 수정 for i in range(length//r + 1) ->
        # 이렇게 바꾸면 if문으로 맨 마지막인지 아닌지 확인하는 과정 없이 맨 마지막이면 알아서 반복문이 종료됨.
        for i in range(r, length, r):
            # 딱 r만큼의 길이만큼 자를 수 있을 때
            # 바로 전과 같은 조합이면 num에 +1
            if prev == s[i:i+r]:
                num += 1

            # 처음 보는 조합이라면 prev 최신화, 이전 조합 new에 반영
            else:
                # 맨 처음엔 그냥 넘겨야 함.
                if prev != '':
                    new += str(num) + prev if num > 1 else prev
                num = 1
                prev = s[i:i+r]

        new += str(num) + prev if num > 1 else prev

        answer = min(answer, len(new))
    return answer

if __name__ == '__main__':
    s = input()
    answer = solution(s)
    print(answer)
    '''