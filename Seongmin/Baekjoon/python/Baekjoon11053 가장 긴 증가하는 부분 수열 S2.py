#백준 11053 가장 긴 증가하는 부분 수열 S2
#LIS 문제인줄 알았으나 DP였음.
# https://bitwise.tistory.com/215 자세한 설명

N = int(input())
arr = list(map(int, input().split()))

LIS = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

print(max(LIS))
