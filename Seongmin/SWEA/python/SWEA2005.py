#SWEA 2005 파스칼의 삼각형
import sys
sys.stdin = open('input.txt', 'r')

# result를 이차원 배열로 만들고, 첫째줄은 [1]
# 다음 줄 부터: 바로 앞 리스트에서 두개씩 더해서 현재 리스트에 더해주면 [1, a, b]의 꼴이 나옴
#  줄의 마지막에 1를 하나 더 추가해준다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))

    arr = [[0] * N for _ in range(N)] #2중 리스트 생성

    for i in range(N): #가장 우측에 있는 수는 항상 1이 되도록.
        arr[i][i] = 1

    for r in range(N):
        for c in range(r):
            if 0 <= r - 1: #행의 첫번째 요소가 아니라면
                arr[r][c] += arr[r - 1][c] #이전 행 값을 더해줌.
                if 0 <= c - 1: #추가로, 열의 첫번째 요소가 아니라면(11사이에 있는 값이라면)
                    arr[r][c] += arr[r - 1][c - 1] #이전 행 값 까지 더해준다.
        print(*arr[r][:r + 1]) #리스트안의 값을 보여줘야하므로 *활용하고, 행번호보다 1개 더 많이 출력해야 하므로 r+1만큼 출력



############ 풀이법 2 이해가 잘 안됨
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     result = [[1]]  #result 첫번째 줄 생성
#
#     for i in range(1, N): #두번째 줄부터 for문 활용하여 생성
#         r = [1]
#         for j in range(len(result[-1]) - 1):
#             sumV = 0
#             for k in range(2):
#                 sumV += result[-1][j + k]
#             r.append(sumV)
#         r.append(1)
#         result.append(r)
#
#     print('#{}'.format(tc))
#     for i in range(len(result)):
#         print(*result[i])





