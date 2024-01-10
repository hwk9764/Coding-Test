n = input()

answer = 0
for idx, chr in enumerate(n):
    if int(chr) != 0 and answer != 0:
        answer *= int(chr)
    else:
        answer += int(chr)
print('answer : ', answer)