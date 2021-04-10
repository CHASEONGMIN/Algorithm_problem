#백준 2667 단지번호붙이기 S1
# 값을 바꾸는 식으로 구현, 델타 활용

import sys
sys.stdin = open('2667.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def chk(x, y):
    global cnt

    arr[x][y] = 0 #방문한 곳 다시 체크 안 되게 값을 바꿈
    cnt += 1

    for i in range(4): #4방 탐색 진행
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= N - 1 and 0 <= yy <= N - 1: #범위 벗어나지 않았을 때
            if arr[xx][yy] == 1: #값이 있으면 진행
                chk(xx, yy)

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
village = []

for r in range(N): #x
    for c in range(N): #y
        if arr[r][c] == 1:
            cnt = 0
            chk(r, c)
            village.append(cnt)

print(len(village))
for i in sorted(village):
    print(i)



