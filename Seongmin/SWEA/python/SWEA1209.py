#SWEA 1209
#sum 2차원 배열 대각선의 합들 중 최댓값 구하기

#가로 - 가로, 세로 - 세로, 대각선 - 대각선간의 합을 더해 최대값을 구하면 됨.
import sys
sys.stdin = open('input.txt', 'r')

for T in range(10): #10개의 테스트 케이스

    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    Max = 0

    # 가로줄의 합 중 최대 값구하기
    m_h = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > m_h:
            m_h = sum

    # 세로줄의 합 중 최대 값구하기
    m_v = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if sum > m_v:
            m_v = sum

    # 대각선의 합 중 최대 값구하기
    m_d = 0
    for i in range(100):
        sum1 = 0;
        sum2 = 0
        sum1 += arr[i][i] # \
        sum2 += arr[i][99 - i]  # /
    if max(sum1, sum2) > m_d:
        m_d = max(sum1, sum2)

    print("#{} {}".format(t,max(m_h, m_v, m_d)))