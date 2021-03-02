#SWEA 4875 미로 D2
#못 품. 코드 찾아봄.
#어려움 복습 필요
#스택활용 풀이 이외에도 DFS로 푸는 풀이있는데 DFS가 더 좋다는듯

import sys
sys.stdin = open('4875.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stack = []
    result = 0
    maze = [list(map(int, list(input()))) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    for i in range(n):   #2인 값, 즉 출발지점 찾기
        for j in range(n):
            if maze[i][j] == 2:
                stack.append((i, j))
                visit[i][j] = 1
    while stack:
        x, y = stack.pop()
        if maze[x][y] == 3:  #도착지점 찾으면 끝
            result = 1
            break
        for i in range(4): #범위를 벗어나지 않았을 때, 지나간적이 없을 때, 값이 0이나 3일 때
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                stack.append((nx, ny))
                visit[nx][ny] = 1
    print('#{} {}'.format(tc, result))
