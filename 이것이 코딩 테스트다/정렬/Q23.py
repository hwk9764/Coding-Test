n = int(input())
graph = []
for _ in range(n):
    name, korean, english, math = input().split()
    graph.append((name, korean, english, math))

# ★★★★★★★★★★★★★★★★★★★★★★
# str은 알아서 아스키코드로 바꾸고 해서 정렬이 되나 봐...
graph.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(graph[i][0])