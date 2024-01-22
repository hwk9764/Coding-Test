# 엄밀히 따지면 bfs/dfs 문제는 아니래. 재귀함수를 썼다는 측면에서 이렇게 분류했다고 함
def solution(p):
    # 1
    if p == '':
        return ''

    num_o = 0  # (
    num_c = 0  # )

    # 2
    for i in range(len(p)):
        if p[i] == '(':
            num_o += 1
        elif p[i] == ')':
            num_c += 1
        if num_o == num_c:
            u = p[:i+1]
            v = p[i+1:]
            break
    # 3
    # 균형잡힌 괄호 문자열이라고 가정할 때, (로 시작하는 애들 중에선 올바른 괄호 문자열이 아닌 경우가 없음 => (와 )의 개수가 정확히 같기 때문에
    if u[0] != ')':
        u += solution(v)
        answer = u

    # 4
    else:
        # 4-1
        answer = '('
        # 4-2, 4-3
        answer += solution(v) + ')'
        # 4-4
        u = u[1:-1]
        for e in u:
            if e == '(':
                answer += ')'
            else:
                answer += '('

    return answer

p = input()
print(solution(p))