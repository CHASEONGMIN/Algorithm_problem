#SWEA 1959 두 개의 숫자열
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    #n, m을 입력받고 각각 리스트 만들어줌
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    result = 0 #결과를 보여주기 위한 값

    #더 긴 리스트 판별
    if n > m:
        for i in range(n - m + 1): #범위 신경써줘야 INDEX error 안남 주의
            tmp = 0
            for j in range(m):  # 짧은 리스트 만큼 돌아줌
                tmp += m_list[j] * n_list[i+j]
            if tmp > result:   #result 와 tmp의 비교를 통해 원하는 결과 도출
                result = tmp
    else:
        for i in range(m - n + 1): #범위 신경써줘야 INDEX error 안남 주의
            tmp = 0
            for j in range(n): # 짧은 리스트 만큼 돌아줌
                tmp += n_list[j] * m_list[i + j]
            if tmp > result:
                result = tmp

    print('#{} {}'.format(tc, result))