#4839 이진탐색

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnta = 0
    cntb = 0


    #이상 초기값 설정

    l = 1
    r = P

    while True:
        c = int((l + r) / 2)
        cnta += 1
        if c == Pa:  #찾음
            break
        elif c <= Pa: #우측에 있는경우
            l = c
        else:  #좌측에 있는경우
            r = c

    l = 1
    r = P
    while True:
        c = int((l + r) / 2)
        cntb += 1
        if c == Pb: #찾음
            break
        elif c <= Pb: #우측에 있는경우
            l = c
        else:
            r = c #좌측에 있는경우

    if cnta == cntb:
        print("#%d %d" % (tc, 0))
    elif cnta > cntb:
        print("#%d %c" % (tc, 'B'))
    else:
        print("#%d %c" % (tc, 'A'))