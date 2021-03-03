#백준1476 날짜 계산 실5
#규칙찾으면 간단한 문제

import sys
E, S, M = map(int, sys.stdin.readline().split())
res = 1

while True: # (res-E), (res-S), (res-M)은 각각 15, 28, 19로 나누어 떨어짐
    if (res - E) % 15 == 0 and (res - S) % 28 == 0 and (res - M) % 19 == 0:
        print(res)
        break
    res += 1
