# 말이 정렬이지 그냥 중간값이 항상 정답이라는 원리로 푸는 문제
# n이 짝수개여서 중간값이 두 개가 나와도 그 두 개의 결과가 같게 나온다
n = int(input())
points = list(map(int, input().split()))
points.sort()

print(points[(n-1)//2])