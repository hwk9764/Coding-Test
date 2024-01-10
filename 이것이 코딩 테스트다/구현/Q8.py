word = list(input())
word.sort()
summation = 0
for com in word:
    if ord('0') < ord(com) <= ord('9'):
        summation += int(com)
    else:
        print(com, end='')
print(summation)