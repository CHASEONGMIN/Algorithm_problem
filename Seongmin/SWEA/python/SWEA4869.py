# SWEA 4869 종이붙이기 D2
# 점화식 (참고함) D(N) = D(N-1) + 2 * D(N-2)
# 이해가 좀 더 필요할 듯


import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

res = [1, 1]  # 초기 f(0)과 f(1)은 1이고, 미리 넣어줘야 추후 활용하기 편하므로 설정

for i in range(2, 51):  # 범위 설정 임의로 50까지로 해줌.
    res.append(res[i - 1] + 2 * res[i - 2])  # 점화식 f(n) = f(n-1) + 2*f(n-2)

for tc in range(1, T + 1):
    N = int(input()) // 10  # 10의 배수를 종이의 폭으로 나눔
    print('#{} {}'.format(tc, res[N]))

# m.append(m[i-1] + 2*m[i-2]) append 활용법 더 많음
# N = int(input())//10 처럼도 사용 가능