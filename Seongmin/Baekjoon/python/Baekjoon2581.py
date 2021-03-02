#백준 2581 소수 실4

M = int(input())
N = int(input())
res = []
for i in range(M, N+1):
    if i != 1:
        Prime = True
        for j in range(2, i):
            if i % j == 0: #i가 j의 배수면 빠르게 멈춰주고 진행
                Prime = False
                break
        if Prime: #소수라면 추가
            res.append(i)
if len(res) == 0: # 아무것도 없으면 -1 출력
    print(-1)
else:
    print(sum(res))
    print(res[0])