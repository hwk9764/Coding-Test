from bisect import bisect_left, bisect_right
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

#words = ["aa", "ac", "az"]
#queries = ["a?"]

# 문제가 너무 어려워서 포기. 내 코드가 위 input으론 잘 나오고, 책의 방법과도 똑같은데
# 프로그래머스에 제출하면 맞는 테스트 케이스가 없다.
# 이 정도 문제는 시험에 나오더라도 포기하기.
def solution(words, queries):
    words.sort()
    answer = [0] * len(queries)
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    reversed_words.sort()
    for idx, q in enumerate(queries):
        num_masking = q.count('?')  # ? 개수
        # 맨 앞부터 masking
        if q[0] == '?':
            masking_end = num_masking - 1  # ? 끝나는 위치
            # 물음표 걷어냄
            char = q[masking_end + 1:]
            left = char + 'a' * num_masking
            right = char + 'z' * num_masking
            start = bisect_left(reversed_words, left)
            end = bisect_right(reversed_words, right)
            for i in reversed_words[start:end + 1]:
                if i[:len(q)-masking_end-1] == char and len(i) == len(q):
                    answer[idx] += 1

        # 맨 뒤부터 masking
        else:
            masking_start = len(q) - num_masking  # ? 제외한 글자 수
            # 물음표 걷어냄
            char = q[:masking_start]  # ? 걷어낸 글자
            left = char + 'a' * num_masking
            right = char + 'z' * num_masking
            start = bisect_left(words, left)
            end = bisect_right(words, right)
            for i in words[start:end + 1]:
                if i[:masking_start] == char and len(i) == len(q):
                    answer[idx] += 1

    return answer

print(solution(words, queries))