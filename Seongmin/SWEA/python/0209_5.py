#SWEA 5789 현주의 상자 바꾸기
# 복습 요망
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        arr[L - 1:R] = [i] * (R - L + 1)
    print('#' + str(tc), " ".join([str(tc) for tc in arr]))

#
# 크기가 n인 배열을 선언해준 뒤, q개의 작업을 받아 반복문의 범위를 L-1<= j <R 로 해주어
# L-1부터 R-1까지의 상자들이 현 작업의 번호로 바뀌게 해줌.
#
#
# Python은 슬라이싱을 통해서 특정 구간의 값을 바꾸기가 매우쉽다.
#
# ▶ Python에서도 index의 시작이 0이므로 arr[L-1:R] 을 통해 배열에서
# 해당 구간을 슬라이싱 한다.
#
# ▶ arr[L-1:R] = [j]*(R-L+1) 을 통해서 슬라이스한 구간을 작업 번호를 나타내는
# j로 R-L+1개 만큼 치환해준다.
#

