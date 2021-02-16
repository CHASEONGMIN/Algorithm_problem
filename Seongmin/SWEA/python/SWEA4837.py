#4837 부분집합의 합

import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    arr = [int(i) for i in range(1, 13)] # 1~12 집합
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1<<len(arr)): # 전체 경우의 수
        sum = 0
        sub = []
        for j in range(len(arr)):
            if i & (1<<j): # 부분 집합
                sub.append(arr[j])
                sum += arr[j]

        if len(sub) == N and sum == K: # N개의 원소를 가진 부분집합의 합이 K일 경우
            cnt += 1

    print("#{} {}".format(tc, cnt))
