#SWEA 1966 숫자를 정렬하자

import sys
sys.stdin = open('input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1): # 1부터인 이유는 아래 # 숫자에서 1부터 나오게 하기 위해서임.
#     # input.split()  - 문자열이므로   map 활용하여 리스트로
#     # list는 확인하기 쉽게 적어줌.
#     n = list(map(int, input().split()))
#     result= []
#     for i in range(len(n) - 1, 0, -1):  # 범위의 끝 위치
#         for j in range(0, i):
#             if n[j] > n[j + 1]:
#                 n[j], n[j + 1] = n[j + 1], n[j]
#         result = result + n
#     print(f'#{tc}', result)

# 내장함수를 이용한 쉬운 풀이

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    #다양한 출력방식 연습 필요
    print('#{}'.format(tc), end=' ')
    for i in range(n):
        print(arr[i], end=' ')
    print()


#내장함수 사용 없이 버블 정렬이용한 코드 추가 예정