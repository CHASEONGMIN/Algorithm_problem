#백준 9506 약수들의 합 브1
#리스트 활용
#좋은 문제

import sys
while True:
    N = int(sys.stdin.readline())
    if N == -1:  # -1이 입력되면 Break
        break
    arr = []  # 약수가 들어갈 리스트
    for i in range(1, N + 1):
        if N % i == 0:  # i가 N의 약수면 리스트에 추가
            arr.append(i)

    tot_i = 0  # 인덱스 0~마지막 전 까지의 합
    for i in arr[:-1]:
        tot_i += i  # 리스트 요소들을 더한다
    if tot_i == N:  # 둘이 같으면 완전수
        res = str(N) + " = " + str(arr[0])
        for i in range(1, len(arr) - 1):
            res += " + " + str(arr[i])
        print(res)
    else:  # 둘이 다르면 완전수 아님
        print(str(arr[-1]) + " is NOT perfect.")