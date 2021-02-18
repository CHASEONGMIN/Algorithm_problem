#SWEA 4861 회문
import sys
sys.stdin = open('sample_input.txt', 'r')

# 가로 탐색 후 세로 탐색
#회문 1개 존재

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    res = [] #결과를 위한 공백 리스트

    str = []  #문자열들을 리스트로
    for _ in range(N):
        str.append(input())

    for i in range(N):  #가로 탐색
        for j in range(N - M + 1):  #
            if str[i][j: j + M] == str[i][j: j + M][:: -1]: #슬라이싱 활용
                res.append(str[i][j: j + M])

    for i in range(N - M + 1):  #세로 탐색
        for j in range(N):
            str2 = []  # 세로줄을 위한 리스트 생성
            for k in range(M):  # 세로줄 입력
                str2.append(str[i + k][j])
            if str2 == str2[:: -1]:  # 회문이면 추가
                res.append(''.join(str2))

    print('#{} {}'.format(test_case, res[0]))