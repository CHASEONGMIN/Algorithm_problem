#백준 2292 벌집 브2
#간단

N = int(input())
cnt = 1
while N > 1:
    N -= (6 * cnt)
    cnt += 1
print(cnt)