#SWEA 4834 숫자 카드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input()
    arr = [int(i) for i in card]
    # arr = list(map(int, input().split())) #카드 리스트 만들기 (잘못 품)
    c = [0] * 10  # 0~9 숫자를 넣을 리스트 생성
    cnt = 0
    num = 0

    for i in arr:
        c[i] += 1

    for j in range(0, 10):
        if cnt <= c[j]:
            num = j
            cnt = c[j]

    print('#{} {} {}'.format(tc, num, cnt))

