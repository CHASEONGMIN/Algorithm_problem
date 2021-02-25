#SWEA 6019 기차 사이의 파리 D3
#기초 수학 문제

import sys
sys.stdin = open('6019.txt', 'r')

for tc in range(1, int(input()) +1):
    D, A, B, F = map(int, input().split())
    #기차 사이 거리, A속력, B속력, 파리 속력
    #거리 = 속 x 시이므로 시간 활용
    Time = D / (A+B)
    ans = F * Time
    print('#{} {:.6f}'.format(tc, ans))  #소수점 출력 포맷팅 :.6f 활용 - 검색