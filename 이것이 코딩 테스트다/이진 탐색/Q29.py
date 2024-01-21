# [공유기 사이 거리를] 이진 탐색으로 찾는 문제.
# mid가 거리고 mid 간격으로 공유기를 설치했을 때 c개를 설치할 수 있으면 mid를 키우고, 없으면 줄임
# 줄이거나 키울 땐 mid를 +1씩, -1씩 하는 게 아니고 start나 end를 조정해서(=>범위를 반으로 줄이며) mid를 많이 키움

n, c = map(int, input().split())
positions = []
for _ in range(n):
    positions.append(int(input()))

positions.sort()

def search(start, end):
    result = 0
    while(start <= end):
        mid = (start+end)//2    # 최단 간격
        count = 1
        prev = positions[0]
        for i in range(1, n):
            if positions[i] >= prev + mid:
                prev = positions[i]
                count += 1
            # 간격 늘리기
            if count == c:
                start = mid + 1
                result = mid
                break
        # 간격 좁히기
        if count < c:
            end = mid - 1
    return result

# start, end를 두 가지 경우로 구해서 최대값을 출력. 앞에서부터 start를 구하는 것과 뒤에서부터 start를 구하는 것이 차이가 있을 수 있고
# start를 어떻게 구하느냐에 따라 따져보는 가능한 경우의 범위가 달라짐.
print(max(search(positions[1]-positions[0], positions[-1]-positions[0]), search(positions[-1]-positions[-2], positions[-1]-positions[0])))