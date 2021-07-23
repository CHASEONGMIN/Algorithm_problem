#백준 11722 가장 긴 감소하는 부분 수열 S2
#LIS, DP.

N = int(input())
arr = list(map(int, input().split()))

LIS = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] > arr[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

print(max(LIS))
