#SWEA 4828
#min, max
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input()) #첫번째
result = 0
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = arr[0]
    max = arr[0]
    for i in range(0, N):
        if max < arr[i]:
            max = arr[i]
            continue
        if min > arr[i]:
            min = arr[i]
            continue
    result = max - min
    print(f'#{tc}', result)


