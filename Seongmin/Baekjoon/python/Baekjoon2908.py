#백준 2909 상수 브2

N, M = map(str, input().split())
N = N[::-1]
M = M[::-1]
res = 0
if int(N) > int(M):
    res = int(N)
else:
    res = int(M)

print(res)

