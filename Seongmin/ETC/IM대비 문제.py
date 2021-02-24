import sys
sys.stdin = open('IM.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    AnswerN = 0
    N = int(input())
    #입력
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            #모든 arr[i][j]를 체크 함
            if arr[i][j] != 'X' and arr[i][j] != 'H':
                #기지국 종류에 따라 반복해줌 (중요)
                for k in range(1, ord(arr[i][j]) - ord('A') + 2):
                    if i + k < N and arr[i+k][j] == 'H': #남
                        arr[i+k][j] = 'X'
                    if j+ k < N and arr[i][j+k] == 'H':  # 동
                        arr[i][j+k] = 'X'
                    if i - k < N and arr[i - k][j] == 'H':  # 북
                        arr[i - k][j] = 'X'
                    if j - k < N and arr[i][j - k] == 'H':  # 서
                        arr[i][j - k] = 'X'

                for k in range(1, ord(arr[i][j]) - ord('B') + 2):
                    if i + k < N and arr[i + k][j] == 'H':  # 남
                        arr[i + k][j] = 'X'
                        arr[i + k +1][j] = 'X'
                    if j + k < N and arr[i][j + k] == 'H':  # 동
                        arr[i][j + k] = 'X'
                        arr[i][j + k + 1] = 'X'
                    if i - k < N and arr[i - k][j] == 'H':  # 북
                        arr[i - k][j] = 'X'
                        arr[i - k - 1][j] = 'X'
                    if j - k < N and arr[i][j - k] == 'H':  # 서
                        arr[i][j - k] = 'X'
                        arr[i][j - k - 1] = 'X'

                for k in range(1, ord(arr[i][j]) - ord('C') + 2):
                    if i + k < N and arr[i + k][j] == 'H':  # 남
                        arr[i + k][j] = 'X'
                        arr[i + k + 1][j] = 'X'
                        arr[i + k + 2][j] = 'X'
                    if j + k < N and arr[i][j + k] == 'H':  # 동
                        arr[i][j + k] = 'X'
                        arr[i][j + k + 1] = 'X'
                        arr[i][j + k + 2] = 'X'
                    if i - k < N and arr[i - k][j] == 'H':  # 북
                        arr[i - k][j] = 'X'
                        arr[i - k -1][j] = 'X'
                        arr[i - k -2][j] = 'X'
                    if j - k < N and arr[i][j - k] == 'H':  # 서
                        arr[i][j - k] = 'X'
                        arr[i][j - k -1] = 'X'
                        arr[i][j - k -2] = 'X'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                AnswerN += 1
    # 출력
    print("#{0} {1}".format(tc, AnswerN))

