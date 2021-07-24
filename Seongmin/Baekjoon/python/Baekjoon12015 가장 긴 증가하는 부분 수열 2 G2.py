#백준 12015 가장 긴 증가하는 부분 수열 2 G2
# 실패, 이분탐색 활용 DP

N = int(input())
arr = list(map(int, input().split()))

LIS = [0]
length = 0

for i in range(N):
    l = 0
    r = len(LIS) -1
    while l <= r:
        m = (l + r) // 2
        if LIS[m] < arr[i]:
            l = m + 1
        else:
            r = m - 1

    if l >= len(LIS):
        LIS.append(arr[i])
    else:
        LIS[l] = arr[i]

print(len(LIS) - 1)
