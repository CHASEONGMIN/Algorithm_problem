#SWEA 1945 간단한 소인수분해
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    cnt = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0

    while True:
        if n % 2 == 0:
            cnt += 1
            n = n // 2
            continue
        if n % 3 == 0:
            cnt2 += 1
            n = n // 3
            continue
        if n % 5 == 0:
            cnt3 += 1
            n = n // 5
            continue
        if n % 7 == 0:
            cnt4 += 1
            n = n // 7
            continue
        if n % 11 == 0:
            cnt5 += 1
            n = n // 11
            continue
        if n == 1:
            break

    print('#{} {} {} {} {} {}'.format(tc, cnt, cnt2, cnt3, cnt4, cnt5))

