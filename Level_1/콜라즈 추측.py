def solution(n):
    cnt = 0
    while (n != 1):
        cnt += 1
        if cnt == 500:
            cnt = -1
            break
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    return cnt
