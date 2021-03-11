# 백준 9095 1,2,3 더하기 S3
#DP, 점화식 찾기
# DP[N] = DP[N-1]+DP[N-2]+DP[N-3]
#못품, 직접 1부터 진행하며 규칙을 찾으면 쉽게 풀 수 있는 문제
import sys

def DP(n):
    if n == 1:
        return 1
    elif n == 2:
        return  2
    elif n == 3:
        return 4
    else:
        return DP(n-1)+DP(n-2)+DP(n-3)

for _ in range(int(sys.stdin.readline())):
    n = int(input())
    print(DP(n))
