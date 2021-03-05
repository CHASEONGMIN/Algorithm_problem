#백준1929 소수 구하기 S2
#에라토스 테네스 체 활용

M, N = map(int, input().split())

ch = [0] * (N+1)


for i in range(2, N+1):
    if ch[i] == 0:
        for j in range(i, N+1, i):
            ch[j] += 1
    else:
        for j in range(i, N+1, i):
            ch[j] += 1

for k in range(M, N+1):
    if ch[k] == 1:
        print(k)
