#백준 2178 미로 S1
#BFS문제, 실패

import sys
sys.stdin = open('2178.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
arr = []  #미로
for i in range(N):
    arr.append(list(input()))

#BFS를 쓰기 위해서 QUEUE사용
queue = []
queue = [[0, 0]]
arr[0][0] = 1

while queue: #답 찾을 때까지
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4): #사방 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] == '1': #경계를 벗어나지 않을 시
            queue.append([xx, yy])
            arr[xx][yy] = arr[x][y] + 1

print(arr[N-1][M-1])



