# SWEA 6485 삼성시의 버스 노선
# 5000개 정류장을 1부터 5000까지 사용한다는걸 보자마자 인덱스가 5001까지임을 확인
# import sys
# sys.stdin = open('s_input.txt', 'r')

# 이하 교수님 풀이
T = int(input())

for tc in range(1, 1 + T):
    # n개의 버스
    N = int(input())

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B + 1):
            bus_stop[j] += 1

    P = int(input())  # 우리가 확인하고 싶은 정류장의 수

    print("#{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())  # 우리가 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end=" ")
    print()

## 출력은 위처럼 하거나 join활용 혹은 *활용 모두 좋음 연습하자



