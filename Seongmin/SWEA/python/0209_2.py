#SWEA 4831 전기버스
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = [0] * (N+1)  #정류장의 수
    arr_num = list(map(int, input().split()))
    for i in arr_num: # 특정 정류장에 충전기 놔두기
        arr[i] += 1
    a = b = result = 0   # a는 이전 장소 b는 현재장소 result는 결과값으로 설정 후 이용할 예정이라 초기화
    b += K  # K만큼 이동

    while True:
        if b >= N:  #종점 도착시 끝
            break
        if arr[b] == 1: # 충전기일 때 1증가
            result += 1
            a = b
            b += K
        else: #충전기가 아닐 때  (종점에 도착할 수 없는 경우)
            b -= 1 # 인덱스를 이전으로 되돌리고
            if a == b:
                result = 0  #결과를 0으로
                break

    print(f'#{tc}', result)