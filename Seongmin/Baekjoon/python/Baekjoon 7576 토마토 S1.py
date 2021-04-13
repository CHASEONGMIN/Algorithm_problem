#백준 7576 토마토 S1
# BFS 대표 문제
# queue 활용

import sys
sys.stdin = open('7576.txt', 'r')
from collections import deque

#4방향 탐색을 위해 dy dx 선언
dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

def bfs(q, cnt):
    count = cnt
    while q:
        a = q.popleft()
        x = a[0]
        y = a[1]
        count = a[2]
        for i in range(4): #4방향 탐색 진행
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m: #경계선 내인지 체크
                if tomato[xx][yy] == 0 and tomato[xx][yy] != -1:
                    tomato[xx][yy] = 1
                    q.append([xx, yy, count+1])
    return count

# 토마토가 모두 익을 수 있는지, 없는지 체크 없으면 -1 출력
def chk(cnt, tomato):
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            if tomato[i][j] == 0:
                return -1
    return cnt

m, n = map(int, input().split())  #가로 세로

# 토마토 리스트 생성
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))

cnt = 0  # 모두 익기까지 걸리는 시간
q = deque([])

# 첫 순회돌며 익은 토마토 큐에 넣어주고 방문 체크
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            q.append([i, j, cnt])
cnt = bfs(q, cnt)

print(chk(cnt, tomato))





