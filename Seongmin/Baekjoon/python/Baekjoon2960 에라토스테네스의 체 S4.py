#백준 2960 에라토스테네스의 체 S4

N, K = map(int, input().split())
ch = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
    if ch[i] == 0:
        for j in range(i, N+1, i):
            if ch[j] == 1:
                continue
            ch[j] += 1
            cnt += 1
            if cnt == K:
                print(j)

