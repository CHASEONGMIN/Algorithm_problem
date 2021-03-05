#SWEA4881 배열 최소 합 D2
#코드 참고함.
import sys
sys.stdin = open('4881.txt', 'r')

def findminimum(idx, total):
    global res #함수에서도 쓰기 위함

    if idx == N:
        if total < result:
            result = total
        return
    if total >= result:  #가지치기 진행해줌.
        return
    for i in range(N):
        # 갔던 세로줄은 사용불가하게 바꾸기
        if visited[i]:
            visited[i] = False
            findminimum(idx + 1, total + arr[idx][i])
            visited[i] = True

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [True for _ in range(N)]
    res = 2160000000 #최소값을 구해야 하므로, 큰수를 넣어줌
    findminimum(0, 0)
    print("#{} {}".format(tc, res))
