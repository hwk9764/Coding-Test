n, k = map(int, input().split())
result = 0
while(True):
    rest = n % k
    mok = n // k
    if n == 1:
        break

    # 더 간략한 방법
    # if n < k:
    #     result += n - 1
    #     n = 1
    #     break
    # elif rest != 0:
    #     n -= rest
    #     result += rest

    # 처음 짠 코드
    elif rest != 0:
        if mok != 0:
            n -= rest
            result += rest
        else:
            n -= rest - 1
            result += rest - 1
    else:
        n //= k
        result += 1
print(result)