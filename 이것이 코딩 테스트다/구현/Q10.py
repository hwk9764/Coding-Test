key = [[0, 0, 1], [0, 0, 1], [0, 1, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    # convolution 모방
    n = len(lock)
    m = len(key)
    new_n = n+2*(m-1)
    # (n+2(m-1), n+2(m-1))짜리 new_lock 만들기
    new_lock = [[-1]*new_n for _ in range(new_n)]
    num_hole = 0
    for i in range(m-1, m-1+n):
        for j in range(m-1, m-1+n):
            new_lock[i][j] = lock[i-(m-1)][j-(m-1)]
            if new_lock[i][j] == 0:
                num_hole += 1
    count = 0
    while(count<4):
        # key 돌리기
        print('돌리기 전 key : ', key)
        key = rotation(key, m)

        for i in range(new_n-m+1):
            for j in range(new_n-m+1):
                temp_lock = [temp[j:j+m] for temp in new_lock[i:i+m]]
                print('temp_lock : ', temp_lock)
                print('key : ', key)
                if test(temp_lock, key, num_hole):
                    return True
        count += 1
    # 세번 돌려가면서 맞춰봤는데도 return을 못했으므로 풀 수 없음
    return False

def rotation(key, m):
    rotate_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotate_key[j][m-i-1] = key[i][j]
    return rotate_key

def test(lock, key, num_hole):
    num_one = 0
    l = len(lock)
    state = False
    for i in range(l):
        for j in range(l):
            '''
            1) 되는 경우
            1. key의 모든 0들이 lock의 1이 만날 때
            2. 동시에 key의 모든 1들이 lock의 1과 만나지 않을 때 => 만나면 키가 안들어감
            2) 안되는 경우
            1. key의 모든 0들이 lock의 1과 만나지 않을 때
            2. key의 1과 lock의 1이 만나는 경우가 존재할 시
            3. key가 lock의 범위 바깥에 있을 때 => lock의 값이 -1일 때'''
            if lock[i][j] == -1:
                print('continue')
                continue
            # 모두가 가능인지 확인하는 것보다 하나라도 불가능일 경우를 따지는 게 더 쉬운 듯
            # 앞 조건은 홈끼리 만날 때, 뒤 조건은 돌기끼리 만날 때
            elif (key[i][j] == 0 and lock[i][j] == 0) or (key[i][j] == 1 and lock[i][j] == 1):
                print('하나라도 안맞는게 존재')
                return False
            elif key[i][j] == 1 and lock[i][j] == 0:
                print('일단 하나는 맞네')
                num_one += 1
            else:
                print('건너 뛰기')
    if num_hole == num_one:
        state = True
    print('test 끝')
    return state

print(solution(key, lock))