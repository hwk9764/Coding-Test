n = int(input())
table = []
for _ in range(n):
    name, grade = input().split()
    table.append((name, int(grade)))

setting = lambda data:data[1]

new_table = sorted(table, key=setting)
for i in range(n):
    print(new_table[i][0], end=' ')
