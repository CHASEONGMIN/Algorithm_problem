#SWEA 2805 농작물 수확하기
#arr = [list(map(int, list(input())))for _ in range(N)] 리스트로 넣어주지 않으면 0이 없음을 주의!!
#arr = [list(map(int, input().strip()))for _ in range(N)] 이것도 가능함.
#중요한 문제
#p와 l이 바뀌면 많이 꼬이므로 조심


import sys
sys.stdin = open('2805.txt', 'r')

#abs(N//2 - i) to abs(N -  p)까지
for tc in range(1, int(input()) + 1):
    res = 0
    N = int(input())
    arr = [list(map(int, list(input())))for _ in range(N)]
    l = N // 2
    p = l # 위치를 바꿔주기 위해 활용할 변수값, 없으면 소프트카피때문에 꼬임 조심
    for i in range(N):
        for j in range(abs(l - i), abs(N - p)):
            res += arr[i][j]
        if i < l:
            p -= 1
        else:
            p += 1

    print('#{} {}'.format(tc, res))

