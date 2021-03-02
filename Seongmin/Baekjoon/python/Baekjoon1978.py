#백준 1978번 소수 찾기 실 4
# 쉬운 문제
N = int(input())
arr = list(map(int, input().split()))
res = 0
for i in arr:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        res += 1
print(res)