num = input()
left = map(int, list(num[:len(num)//2]))
right = map(int, list(num[len(num)//2:]))

left = sum(left)
right = sum(right)

if left == right:
    print("lucky")
else:
    print('ready')