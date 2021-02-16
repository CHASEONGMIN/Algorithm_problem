#4836 색칠하기 문제

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 칠할 영역의 개수
    arr = [[0] * 10 for i in range(10)] # 배열 초기화 1
    # arr = [[0 for _ in range(10)] for _ in range(10)] #배열 초기화 2

    cnt = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 +1):
            for c in range(c1, c2 +1):
                if color == 1:   # color = 1일때
                    if arr[r][c] == 0:
                        arr[r][c] = 1
                    elif arr[r][c] == 2: #중복 시 3으로
                        arr[r][c] = 3
                        cnt += 1
                else:
                    if arr[r][c] == 0:
                        arr[r][c] = 2
                    elif arr[r][c] == 1:
                        arr[r][c] = 3
                        cnt += 1

    print('#{} {}'.format(tc, cnt))