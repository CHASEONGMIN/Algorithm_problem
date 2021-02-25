#백준 1913 달팽이 실5
#연습하기에 좋은 문제.

#가면서 못가는 곳이 있을때 방향을 바꾼다.
#제약 조건을 설계하는데 있어 반대방향으로 가는게 좋다. while(now_num > 0)
#벽은 x < 0, x >= n, y < 0, y >= n, 그리고 방안에 들어가 있는 값이 0이 아닐 경우 벽으로 간주한다.
#벽에 부딪혔을 때, 방향을 바꾸는데, 이 순서를 0, 1, 2, 3으로 설정해두고 바꾼다.
#거꾸로 시작했으므로 아래, 오른쪽, 위, 왼쪽 이 반복될 것

N = int(input())
w = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
num = 1

x = y = N // 2
check = 2
arr[x][y] = num
i = 0
j = 0
while arr[0][0] != N ** 2:
    x -= 1
    for i in range(check):
        num += 1
        arr[x][y + i] = num
        if num == w:
            ans = [x + 1, y + i + 1]
    y += i
    for i in range(1, check + 1):
        num += 1
        arr[x + i][y] = num
        if num == w:
            ans = [x + i + 1, y + 1]
    x += i
    for i in range(1, check + 1):
        num += 1
        arr[x][y - i] = num
        if num == w:
            ans = [x + 1, y - i + 1]
    y -= i
    for i in range(1, check + 1):
        num += 1
        arr[x - i][y] = num
        if num == w:
            ans = [x - i + 1, y + 1]
    x -= i
    check += 2

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
print(*ans)