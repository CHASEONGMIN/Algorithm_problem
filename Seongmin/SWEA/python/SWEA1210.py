#SWEA 1210 Ladder1
#핵심 : 위에서 아래로 가면 여러번의 시도를 해야하지만, 아래 2로부터 올라가면 한번의 시도만 하면 찾을 수 있음
import sys
sys.stdin = open('input.txt', 'r')

T = 10 #10개의 테스트 케이스 주어짐
for tc in range(T):
    a = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)] #배열 생성

    y = N-1  #y값의 인덱스는 제일 아래인 99부터 시작
    x = arr[N-1].index(2) #index가 2인 값의 x값의 인덱스
    num = 0

    # while문을 활용해주는 것이 좋음 (특정 상황이 아니면 직진해야하니)
    while y > 0: #y 인덱스가 0이 될 때의 x의 좌표를 구해야 하므로
        if (num == 0 or num == 1) and x > 0 and arr[y][x-1]: #왼쪽에 값이 1이라면
            x -= 1
            num = 1
        elif (num == 0 or num == 3) and x < N-1 and arr[y][x+1]: #우측 값이 1이라면 구별을 해주기 위해 3으로 설정해줌
            x += 1
            num = 3
        else:
            y -= 1
            num = 0
    print("#{} {}".format(a, x))
