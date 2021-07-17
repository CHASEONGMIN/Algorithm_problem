#백준 11659 구간 합 구하기 4 S3
# 누적합, 단순하게 매번 구하면 시간 초과 남
# 중요! 주어진 구간을 i, j라고 할 때, i부터 j까지의 구간 합을 S[j] - S[i - 1]으로 표현할 수 있음.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = [0]
sum = 0

for i in range(len(arr)):
    sum += arr[i]
    sum_list.append(sum)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])