#SWEA 1945 간단한 소인수분해
import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#
#     n = int(input())
#     cnt = 0
#     cnt2 = 0
#     cnt3 = 0
#     cnt4 = 0
#     cnt5 = 0
#
#     while True:
#         if n % 2 == 0:
#             cnt += 1
#             n = n // 2
#             continue
#         if n % 3 == 0:
#             cnt2 += 1
#             n = n // 3
#             continue
#         if n % 5 == 0:
#             cnt3 += 1
#             n = n // 5
#             continue
#         if n % 7 == 0:
#             cnt4 += 1
#             n = n // 7
#             continue
#         if n % 11 == 0:
#             cnt5 += 1
#             n = n // 11
#             continue
#         if n == 1:
#             break
#
#     print('#{} {} {} {} {} {}'.format(tc, cnt, cnt2, cnt3, cnt4, cnt5))

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    prime = [2, 3, 5, 7, 11]

    cnt = [0] * 5 #정답을 위한 개수 세기

    #주어진 소수의 수만큼 반복
    for i in range(len(prime)):
        while N % prime[i] == 0:
            cnt[i] += 1
            N //= prime[i]
    print('#{} {}'.format(tc, " ".join(map(str, cnt))))
    #join을 쓰기 위해 문자열이 필요하므로 map을 활용하여 숫자를 문자열로 만들고 이를이용해 출력