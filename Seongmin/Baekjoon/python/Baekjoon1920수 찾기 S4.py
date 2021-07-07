#백준 1920 수 찾기 S4 이분탐색

import sys

# 1. 정렬
n = int(sys.stdin.readline())
N = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

# 이분 탐색 진행
for i in M:
    l = 0
    r = n
    while l <= r:
        mid = (l+r)//2
        if mid < n and mid > -1:
            if N[mid] < i:
                l = mid+1
            else:
                r = mid-1
        else:
            break
    if mid < n and mid > -1:
        if i == N[r+1]:
            print(1)
        else:
            print(0)
    else:
        print(0)

'''
재귀를 활용하는 방법이 시간을 고려했을 때 많이 좋았음.
대표적 풀이

from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))

'''
