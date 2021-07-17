#백준 11403 경로찾기 S1
# 플로이드 - 워셜 알고리즘

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

#플로이드 워셜 알고리즘 이용
for k in range(0, n) :
    for i in range(0, n) :
        for j in range(0, n):
            if arr[i][k] and arr[k][j] :
                arr[i][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
